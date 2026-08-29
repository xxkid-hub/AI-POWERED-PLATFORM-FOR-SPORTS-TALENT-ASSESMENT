#!/usr/bin/env python3
"""
ApexScout AI - Custom Multi-Sport Model Training Pipeline
Trains a custom Machine Learning & Kinematic Feature Model directly on the dataset/ directory
across Athletics, Basketball, Cricket, Kabaddi, Soccer, and Volleyball.
"""

import os
import sys
import glob
import json
import time
import numpy as np
from PIL import Image

# Ensure UTF-8 output encoding on Windows stdout
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_DIR = os.path.join(BASE_DIR, "dataset")
MODEL_DIR = os.path.join(BASE_DIR, "trained_model")
os.makedirs(MODEL_DIR, exist_ok=True)

SPORTS_CATEGORIES = [
    "Athletics",
    "Basketball",
    "Cricket",
    "Kabaddi",
    "Soccer",
    "Volleyball"
]

def extract_features_from_image(img_path, target_size=(48, 48)):
    """
    Extracts a robust 74-dimensional feature vector combining:
    1. Spatial Color Moments (RGB channel means, stds, medians)
    2. Spatial 3x3 block luminance grid
    3. Horizontal & Vertical Edge Gradients (Sobel approximation)
    4. Center of Mass (cx, cy) and Horizontal / Vertical Symmetry Indices
    5. Texture Energy Moments
    """
    try:
        with Image.open(img_path) as raw_img:
            img = raw_img.convert("RGB").resize(target_size, Image.BILINEAR)
            arr = np.array(img, dtype=np.float32) / 255.0  # (48, 48, 3)
            
            features = []
            
            # 1. Color Channel Statistics (RGB - 9 features)
            for c in range(3):
                channel = arr[:, :, c]
                features.append(float(np.mean(channel)))
                features.append(float(np.std(channel)))
                features.append(float(np.median(channel)))
                
            # 2. Grayscale Luminance (48, 48)
            gray = 0.2989 * arr[:, :, 0] + 0.5870 * arr[:, :, 1] + 0.1140 * arr[:, :, 2]
            
            # Spatial 3x3 block luminance (9 blocks x 2 = 18 features)
            h, w = gray.shape
            bh, bw = h // 3, w // 3
            for i in range(3):
                for j in range(3):
                    block = gray[i*bh:(i+1)*bh, j*bw:(j+1)*bw]
                    features.append(float(np.mean(block)))
                    features.append(float(np.std(block)))
                    
            # 3. Discrete Gradients (2D Sobel)
            dx = np.diff(gray, axis=1)  # (48, 47)
            dy = np.diff(gray, axis=0)  # (47, 48)
            
            grad_mag_x = np.abs(dx)
            grad_mag_y = np.abs(dy)
            
            features.append(float(np.mean(grad_mag_x)))
            features.append(float(np.std(grad_mag_x)))
            features.append(float(np.mean(grad_mag_y)))
            features.append(float(np.std(grad_mag_y)))
            
            # 4. 8-Bin Orientation Energy
            # Pad dx and dy to same shape
            dx_pad = np.zeros_like(gray)
            dy_pad = np.zeros_like(gray)
            dx_pad[:, :-1] = dx
            dy_pad[:-1, :] = dy
            
            mag = np.sqrt(dx_pad**2 + dy_pad**2)
            ori = (np.arctan2(dy_pad, dx_pad) + np.pi) % np.pi  # [0, pi]
            hist, _ = np.histogram(ori, bins=8, range=(0, np.pi), weights=mag)
            hist_norm = hist / (np.linalg.norm(hist) + 1e-6)
            features.extend(hist_norm.tolist())  # 8 features
            
            # 4 quadrants x 4 bins = 16 features
            qh, qw = h // 2, w // 2
            for qi in range(2):
                for qj in range(2):
                    q_mag = mag[qi*qh:(qi+1)*qh, qj*qw:(qj+1)*qw]
                    q_ori = ori[qi*qh:(qi+1)*qh, qj*qw:(qj+1)*qw]
                    q_hist, _ = np.histogram(q_ori, bins=4, range=(0, np.pi), weights=q_mag)
                    q_hist_norm = q_hist / (np.linalg.norm(q_hist) + 1e-6)
                    features.extend(q_hist_norm.tolist())
                    
            # 5. Center of Mass & Geometric Symmetry (4 features)
            y_coords, x_coords = np.mgrid[0:h, 0:w]
            total_mass = np.sum(gray) + 1e-6
            cy = float(np.sum(y_coords * gray) / total_mass) / h
            cx = float(np.sum(x_coords * gray) / total_mass) / w
            
            left_half = gray[:, :w//2]
            right_half_flipped = np.fliplr(gray[:, w//2:])
            symmetry_lr = float(np.mean(np.abs(left_half - right_half_flipped)))
            
            top_half = gray[:h//2, :]
            bottom_half_flipped = np.flipud(gray[h//2:, :])
            symmetry_tb = float(np.mean(np.abs(top_half - bottom_half_flipped)))
            
            features.extend([cx, cy, symmetry_lr, symmetry_tb])
            
            # 6. Peak Energy Percentiles (3 features)
            features.append(float(np.percentile(gray, 95)))
            features.append(float(np.percentile(gray, 50)))
            features.append(float(np.percentile(gray, 5)))
            
            return np.array(features, dtype=np.float32)
            
    except Exception as e:
        print(f"[!] Feature extraction error on {img_path}: {e}", flush=True)
        return None

def load_dataset():
    print("\n[1/4] Scanning and extracting features from dataset/ ...", flush=True)
    X = []
    y = []
    sample_paths = []
    
    for label_idx, sport in enumerate(SPORTS_CATEGORIES):
        sport_dir = os.path.join(DATASET_DIR, sport)
        if not os.path.exists(sport_dir):
            continue
            
        img_files = glob.glob(os.path.join(sport_dir, "*.png"))
        print(f"  -> {sport:12s}: Extracting features for {len(img_files)} images...", flush=True)
        
        for f in img_files:
            feats = extract_features_from_image(f)
            if feats is not None:
                X.append(feats)
                y.append(label_idx)
                sample_paths.append(f)
                
    X = np.array(X, dtype=np.float32)
    y = np.array(y, dtype=np.int32)
    print(f"  [+] Loaded total {len(X)} samples with {X.shape[1]} features each.", flush=True)
    return X, y, sample_paths

def train_and_evaluate():
    start_time = time.time()
    print("=" * 65, flush=True)
    print(" [ApexScout AI] - Custom Sports Model Training Pipeline", flush=True)
    print("=" * 65, flush=True)
    
    X, y, sample_paths = load_dataset()
    if len(X) == 0:
        print("[X] Error: No samples loaded from dataset.", flush=True)
        return
        
    print(f"\n[2/4] Normalizing and splitting dataset (80% Train, 20% Test)...", flush=True)
    
    try:
        from sklearn.model_selection import train_test_split
        from sklearn.preprocessing import StandardScaler
        from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, VotingClassifier
        from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
        import joblib
        
        # Stratified 80/20 train/test split
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.20, random_state=42, stratify=y
        )
        
        # Standard Scaler
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        print("\n[3/4] Training Ensemble Multi-Sport Classifier (RandomForest + ExtraTrees)...", flush=True)
        rf = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42, n_jobs=1)
        et = ExtraTreesClassifier(n_estimators=100, max_depth=10, random_state=42, n_jobs=1)
        
        ensemble = VotingClassifier(
            estimators=[('rf', rf), ('et', et)],
            voting='soft'
        )
        
        ensemble.fit(X_train_scaled, y_train)
        
        # Evaluation
        print("\n[4/4] Evaluating model performance on Hold-Out Test Set...", flush=True)
        y_pred = ensemble.predict(X_test_scaled)
        
        acc = accuracy_score(y_test, y_pred)
        conf_matrix = confusion_matrix(y_test, y_pred).tolist()
        class_report = classification_report(
            y_test, y_pred, target_names=SPORTS_CATEGORIES, output_dict=True
        )
        
        print(f"\n" + "=" * 65, flush=True)
        print(f" [RESULT] Overall Test Accuracy: {acc * 100:.2f}%", flush=True)
        print("=" * 65, flush=True)
        for sport in SPORTS_CATEGORIES:
            metrics = class_report[sport]
            print(f"  {sport:12s} | Precision: {metrics['precision']:.3f} | Recall: {metrics['recall']:.3f} | F1: {metrics['f1-score']:.3f}", flush=True)
            
        # Save model and artifacts
        model_save_path = os.path.join(MODEL_DIR, "sports_talent_model.joblib")
        scaler_save_path = os.path.join(MODEL_DIR, "feature_scaler.joblib")
        
        joblib.dump(ensemble, model_save_path)
        joblib.dump(scaler, scaler_save_path)
        
        # Save Metadata & Evaluation Report
        report_path = os.path.join(MODEL_DIR, "evaluation_report.json")
        report_data = {
            "model_name": "ApexScout Ensemble Multi-Sport Kinematic Classifier",
            "algorithm": "VotingClassifier (RandomForest + ExtraTrees)",
            "trained_at": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "training_duration_seconds": round(time.time() - start_time, 2),
            "total_samples": int(len(X)),
            "train_samples": int(len(X_train)),
            "test_samples": int(len(X_test)),
            "feature_dimension": int(X.shape[1]),
            "overall_accuracy": round(float(acc), 4),
            "classes": SPORTS_CATEGORIES,
            "confusion_matrix": conf_matrix,
            "classification_report": class_report
        }
        
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(report_data, f, indent=2)
            
        print(f"\n[+] Trained model saved to: {model_save_path}", flush=True)
        print(f"[+] Scaler saved to: {scaler_save_path}", flush=True)
        print(f"[+] Evaluation report saved to: {report_path}", flush=True)
        print(f"[+] Total Training Duration: {time.time() - start_time:.2f}s", flush=True)
        print("=" * 65, flush=True)
        
    except Exception as err:
        print(f"[!] Training error: {err}", flush=True)

if __name__ == "__main__":
    train_and_evaluate()
