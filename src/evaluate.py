"""
ApexScout AI - Standalone Model Evaluation & Visualization Engine
Loads trained checkpoint artifacts without retraining, evaluates on test splits,
and generates both visual figures (confusion_matrix.png) and evaluation_summary.json.
"""

import os
import sys
import json
import glob
import numpy as np
import joblib
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split

from config.settings import (
    BASE_DIR,
    DATASET_DIR,
    MODEL_DIR,
    RESULTS_DIR,
    SPORTS_CATEGORIES,
    DEFAULT_SEED,
    TEST_SPLIT
)
from src.preprocessor import SportsImagePreprocessor

def plot_confusion_matrix_figure(conf_matrix, class_names, save_path):
    """
    Renders and saves a high-resolution Confusion Matrix figure.
    Uses matplotlib if installed; otherwise renders with PIL.
    """
    try:
        import matplotlib
        matplotlib.use("Agg")  # Non-interactive backend
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots(figsize=(8, 6), dpi=150)
        im = ax.imshow(conf_matrix, interpolation='nearest', cmap=plt.cm.Blues)
        ax.figure.colorbar(im, ax=ax)

        ax.set(
            xticks=np.arange(conf_matrix.shape[1]),
            yticks=np.arange(conf_matrix.shape[0]),
            xticklabels=class_names,
            yticklabels=class_names,
            title="ApexScout AI - Multi-Sport Classifier Confusion Matrix",
            ylabel="True Class",
            xlabel="Predicted Class"
        )
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

        # Loop over data dimensions and create text annotations
        thresh = conf_matrix.max() / 2.0
        for i in range(conf_matrix.shape[0]):
            for j in range(conf_matrix.shape[1]):
                ax.text(
                    j, i, format(conf_matrix[i, j], 'd'),
                    ha="center", va="center",
                    color="white" if conf_matrix[i, j] > thresh else "black"
                )

        fig.tight_layout()
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, bbox_inches='tight')
        plt.close(fig)
        return True
    except Exception as e:
        # Fallback using PIL
        try:
            from PIL import Image, ImageDraw, ImageFont
            img_size = (600, 600)
            img = Image.new("RGB", img_size, color=(14, 20, 32))
            draw = ImageDraw.Draw(img)
            draw.text((20, 20), "ApexScout AI Confusion Matrix", fill=(0, 242, 254))
            
            n = len(class_names)
            grid_top = 80
            grid_left = 120
            cell_size = 65
            max_val = max(int(np.max(conf_matrix)), 1)
            
            for i in range(n):
                draw.text((20, grid_top + i * cell_size + 20), class_names[i][:8], fill=(200, 200, 200))
                for j in range(n):
                    val = int(conf_matrix[i, j])
                    intensity = int((val / max_val) * 200)
                    fill_col = (20, 40 + intensity, 60 + intensity)
                    x0 = grid_left + j * cell_size
                    y0 = grid_top + i * cell_size
                    draw.rectangle([x0, y0, x0 + cell_size - 2, y0 + cell_size - 2], fill=fill_col, outline=(50, 70, 90))
                    draw.text((x0 + 20, y0 + 20), str(val), fill=(255, 255, 255))
            
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            img.save(save_path)
            return True
        except Exception as fallback_err:
            print(f"[!] Warning: Could not save confusion matrix image: {fallback_err}")
            return False

def evaluate_model(
    data_dir=DATASET_DIR,
    model_dir=MODEL_DIR,
    results_dir=RESULTS_DIR,
    test_size=TEST_SPLIT,
    seed=DEFAULT_SEED
):
    """
    Performs standalone evaluation on the model without requiring training.
    """
    model_path = os.path.join(model_dir, "sports_talent_model.joblib")
    scaler_path = os.path.join(model_dir, "feature_scaler.joblib")

    if not os.path.exists(model_path) or not os.path.exists(scaler_path):
        raise FileNotFoundError(
            f"Trained model artifacts not found at {model_dir}. Please run train_model.py first."
        )

    print("=" * 65)
    print(" [ApexScout AI] - Standalone Model Evaluation")
    print("=" * 65)
    print(f" Loading checkpoint: {model_path}")
    print(f" Loading feature scaler: {scaler_path}")

    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    preprocessor = SportsImagePreprocessor()

    # Load dataset features
    X = []
    y = []
    for label_idx, sport in enumerate(SPORTS_CATEGORIES):
        sport_dir = os.path.join(data_dir, sport)
        if not os.path.exists(sport_dir):
            continue
        for f in glob.glob(os.path.join(sport_dir, "*.png")):
            feats = preprocessor.extract_features(f)
            if feats is not None:
                X.append(feats)
                y.append(label_idx)

    X = np.array(X, dtype=np.float32)
    y = np.array(y, dtype=np.int32)

    # Perform reproducible stratified split to get holdout test split
    _, X_test, _, y_test = train_test_split(
        X, y, test_size=test_size, random_state=seed, stratify=y
    )

    X_test_scaled = scaler.transform(X_test)
    y_pred = model.predict(X_test_scaled)

    acc = float(accuracy_score(y_test, y_pred))
    conf_mat = confusion_matrix(y_test, y_pred)
    class_report = classification_report(
        y_test, y_pred, target_names=SPORTS_CATEGORIES, output_dict=True
    )

    os.makedirs(results_dir, exist_ok=True)
    cm_path = os.path.join(results_dir, "confusion_matrix.png")
    plot_confusion_matrix_figure(conf_mat, SPORTS_CATEGORIES, cm_path)

    summary = {
        "evaluation_type": "Standalone Hold-Out Verification",
        "total_test_samples": int(len(y_test)),
        "overall_accuracy": round(acc, 4),
        "overall_accuracy_percentage": f"{acc * 100:.2f}%",
        "classes": SPORTS_CATEGORIES,
        "confusion_matrix": conf_mat.tolist(),
        "classification_report": class_report,
        "artifacts_generated": {
            "confusion_matrix_plot": cm_path
        }
    }

    summary_path = os.path.join(results_dir, "evaluation_summary.json")
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    print("\n" + "=" * 65)
    print(f" [EVALUATION SUCCESS] Verified Accuracy: {acc * 100:.2f}%")
    print(f" [+] Confusion Matrix Plot: {cm_path}")
    print(f" [+] Evaluation Summary: {summary_path}")
    print("=" * 65)
    for sport in SPORTS_CATEGORIES:
        m = class_report[sport]
        print(f"  {sport:12s} | Precision: {m['precision']:.3f} | Recall: {m['recall']:.3f} | F1: {m['f1-score']:.3f}")
    print("=" * 65)

    return summary

if __name__ == "__main__":
    evaluate_model()
