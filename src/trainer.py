"""
ApexScout AI - Modular Model Trainer & Checkpointing Engine
Includes deterministic seed-setting, stratified dataset loading,
VotingClassifier ensemble training, and artifact persistence.
"""

import os
import sys
import glob
import json
import time
import random
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, VotingClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

from config.settings import (
    BASE_DIR,
    DATASET_DIR,
    MODEL_DIR,
    SPORTS_CATEGORIES,
    DEFAULT_SEED,
    TEST_SPLIT,
    get_config
)
from src.preprocessor import SportsImagePreprocessor

def seed_everything(seed=DEFAULT_SEED):
    """
    Enforces deterministic random state across Python, NumPy, and optional frameworks.
    """
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)
    try:
        import torch
        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)
            torch.backends.cudnn.deterministic = True
    except ImportError:
        pass
    return seed

class SportsModelTrainer:
    """
    Modular Trainer for ApexScout AI Multi-Sport Kinematic Model.
    """

    def __init__(self, data_dir=DATASET_DIR, model_dir=MODEL_DIR, config=None, seed=DEFAULT_SEED):
        self.data_dir = data_dir
        self.model_dir = model_dir
        self.config = config or get_config()
        self.seed = seed
        self.preprocessor = SportsImagePreprocessor(
            target_size=self.config.get("data", {}).get("target_size", (48, 48))
        )
        os.makedirs(self.model_dir, exist_ok=True)

    def load_dataset(self):
        """
        Scans categories in data_dir, extracts features, and returns X, y, sample_paths.
        """
        categories = self.config.get("data", {}).get("categories", SPORTS_CATEGORIES)
        X = []
        y = []
        sample_paths = []

        print(f"\n[1/4] Scanning & feature-extracting dataset at: {self.data_dir}", flush=True)

        for label_idx, sport in enumerate(categories):
            sport_dir = os.path.join(self.data_dir, sport)
            if not os.path.exists(sport_dir):
                continue

            img_files = glob.glob(os.path.join(sport_dir, "*.png"))
            print(f"  -> {sport:12s}: Extracting {len(img_files)} images...", flush=True)

            for f in img_files:
                feats = self.preprocessor.extract_features(f)
                if feats is not None:
                    X.append(feats)
                    y.append(label_idx)
                    sample_paths.append(f)

        X = np.array(X, dtype=np.float32)
        y = np.array(y, dtype=np.int32)
        print(f"  [+] Loaded total {len(X)} samples with {X.shape[1] if len(X) > 0 else 0} features each.", flush=True)
        return X, y, sample_paths

    def train(self, test_size=TEST_SPLIT, n_estimators_rf=100, n_estimators_et=100, max_depth=10):
        """
        Executes complete training pipeline, hold-out validation, and saves artifacts.
        """
        start_time = time.time()
        seed_everything(self.seed)

        print("=" * 65, flush=True)
        print(" [ApexScout AI] - Sports Model Trainer Pipeline", flush=True)
        print(f" Deterministic Random Seed: {self.seed}", flush=True)
        print("=" * 65, flush=True)

        X, y, sample_paths = self.load_dataset()
        if len(X) == 0:
            raise ValueError(f"No samples found in dataset directory: {self.data_dir}")

        categories = self.config.get("data", {}).get("categories", SPORTS_CATEGORIES)

        print(f"\n[2/4] Stratified Dataset Split (Train {int((1-test_size)*100)}% / Test {int(test_size*100)}%)...", flush=True)
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=self.seed, stratify=y
        )

        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        print(f"\n[3/4] Training Soft-Voting Ensemble (RandomForest + ExtraTrees)...", flush=True)
        rf = RandomForestClassifier(
            n_estimators=n_estimators_rf,
            max_depth=max_depth,
            random_state=self.seed,
            n_jobs=1
        )
        et = ExtraTreesClassifier(
            n_estimators=n_estimators_et,
            max_depth=max_depth,
            random_state=self.seed,
            n_jobs=1
        )

        ensemble = VotingClassifier(
            estimators=[('rf', rf), ('et', et)],
            voting='soft'
        )
        ensemble.fit(X_train_scaled, y_train)

        print(f"\n[4/4] Evaluating Model on Hold-Out Test Split...", flush=True)
        y_pred = ensemble.predict(X_test_scaled)
        acc = float(accuracy_score(y_test, y_pred))
        conf_mat = confusion_matrix(y_test, y_pred).tolist()
        class_report = classification_report(
            y_test, y_pred, target_names=categories, output_dict=True
        )

        print(f"\n" + "=" * 65, flush=True)
        print(f" [RESULT] Overall Test Accuracy: {acc * 100:.2f}%", flush=True)
        print("=" * 65, flush=True)
        for sport in categories:
            m = class_report[sport]
            print(f"  {sport:12s} | Precision: {m['precision']:.3f} | Recall: {m['recall']:.3f} | F1: {m['f1-score']:.3f}", flush=True)

        # Save artifacts
        model_path = os.path.join(self.model_dir, "sports_talent_model.joblib")
        scaler_path = os.path.join(self.model_dir, "feature_scaler.joblib")
        report_path = os.path.join(self.model_dir, "evaluation_report.json")

        joblib.dump(ensemble, model_path)
        joblib.dump(scaler, scaler_path)

        report_data = {
            "model_name": "ApexScout Ensemble Multi-Sport Kinematic Classifier",
            "algorithm": "VotingClassifier (RandomForest + ExtraTrees)",
            "trained_at": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "training_duration_seconds": round(time.time() - start_time, 2),
            "random_seed": self.seed,
            "total_samples": int(len(X)),
            "train_samples": int(len(X_train)),
            "test_samples": int(len(X_test)),
            "feature_dimension": int(X.shape[1]),
            "overall_accuracy": round(acc, 4),
            "classes": categories,
            "confusion_matrix": conf_mat,
            "classification_report": class_report
        }

        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(report_data, f, indent=2)

        print(f"\n[+] Trained model saved to: {model_path}", flush=True)
        print(f"[+] Scaler saved to: {scaler_path}", flush=True)
        print(f"[+] Evaluation report saved to: {report_path}", flush=True)
        print("=" * 65, flush=True)

        return {
            "model": ensemble,
            "scaler": scaler,
            "accuracy": acc,
            "report_data": report_data,
            "X_test": X_test,
            "y_test": y_test,
            "X_test_scaled": X_test_scaled,
            "y_pred": y_pred
        }
