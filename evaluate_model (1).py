"""
ApexScout AI - Model Evaluation
Evaluates the trained sports talent classification model.

Expected project structure:
    trained_model/
        sports_talent_model.joblib
        feature_scaler.joblib
    dataset/
        athletics/
        basketball/
        cricket/
        kabaddi/
        soccer/
        volleyball/
"""

from pathlib import Path
import json
import joblib
import numpy as np
from PIL import Image
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix,
)

# -------------------------------------------------------------------
# Paths
# -------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
DATASET_DIR = BASE_DIR / "dataset"
MODEL_DIR = BASE_DIR / "trained_model"

MODEL_PATH = MODEL_DIR / "sports_talent_model.joblib"
SCALER_PATH = MODEL_DIR / "feature_scaler.joblib"

SPORTS = [
    "athletics",
    "basketball",
    "cricket",
    "kabaddi",
    "soccer",
    "volleyball",
]

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}


# -------------------------------------------------------------------
# Feature extraction
# NOTE:
# This function should match the feature extraction used in
# train_model.py. If train_model.py is changed, update this function
# accordingly.
# -------------------------------------------------------------------
def extract_features(image_path):
    image = Image.open(image_path).convert("RGB").resize((48, 48))
    img = np.asarray(image, dtype=np.float32) / 255.0

    features = []

    # RGB statistics
    for channel in range(3):
        c = img[:, :, channel]
        features.extend([
            float(c.mean()),
            float(c.std()),
            float(c.min()),
            float(c.max()),
        ])

    # Luminance statistics
    luminance = (
        0.299 * img[:, :, 0]
        + 0.587 * img[:, :, 1]
        + 0.114 * img[:, :, 2]
    )

    features.extend([
        float(luminance.mean()),
        float(luminance.std()),
        float(np.percentile(luminance, 25)),
        float(np.percentile(luminance, 50)),
        float(np.percentile(luminance, 75)),
    ])

    # Spatial block statistics
    h, w = luminance.shape
    for rows, cols in [(2, 2), (4, 4)]:
        for r in range(rows):
            for c in range(cols):
                block = luminance[
                    r * h // rows:(r + 1) * h // rows,
                    c * w // cols:(c + 1) * w // cols,
                ]
                features.extend([
                    float(block.mean()),
                    float(block.std()),
                ])

    # Gradient features
    gx = np.diff(luminance, axis=1)
    gy = np.diff(luminance, axis=0)

    features.extend([
        float(np.abs(gx).mean()),
        float(np.abs(gx).std()),
        float(np.abs(gy).mean()),
        float(np.abs(gy).std()),
    ])

    # Center of mass
    yy, xx = np.indices(luminance.shape)
    weight = luminance + 1e-8
    total = weight.sum()

    features.extend([
        float((xx * weight).sum() / total / w),
        float((yy * weight).sum() / total / h),
    ])

    # Symmetry
    flipped = np.fliplr(luminance)
    symmetry_error = np.abs(luminance - flipped)

    features.extend([
        float(symmetry_error.mean()),
        float(symmetry_error.std()),
    ])

    # Intensity percentiles
    for p in [5, 10, 25, 50, 75, 90, 95]:
        features.append(float(np.percentile(luminance, p)))

    # Keep this assertion visible so a mismatch with train_model.py
    # is caught instead of silently producing a wrong evaluation.
    return np.asarray(features, dtype=np.float32)


def load_dataset():
    X = []
    y = []

    for sport in SPORTS:
        sport_dir = DATASET_DIR / sport

        if not sport_dir.exists():
            print(f"WARNING: Missing dataset folder: {sport_dir}")
            continue

        for image_path in sorted(sport_dir.rglob("*")):
            if image_path.suffix.lower() not in IMAGE_EXTENSIONS:
                continue

            try:
                features = extract_features(image_path)
                X.append(features)
                y.append(sport)
            except Exception as exc:
                print(f"Skipping {image_path}: {exc}")

    if not X:
        raise RuntimeError(
            f"No images found in {DATASET_DIR}. "
            "Check your dataset folders."
        )

    return np.vstack(X), np.asarray(y)


def main():
    print("=" * 60)
    print("ApexScout AI - Model Evaluation")
    print("=" * 60)

    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Model not found: {MODEL_PATH}\n"
            "Run train_model.py first."
        )

    if not SCALER_PATH.exists():
        raise FileNotFoundError(
            f"Scaler not found: {SCALER_PATH}\n"
            "Run train_model.py first."
        )

    print("\nLoading model...")
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)

    print("Loading dataset...")
    X, y = load_dataset()

    print(f"Total samples: {len(y)}")
    print(f"Feature count: {X.shape[1]}")

    # Use the same stratified 80/20 split used for model training.
    _, X_test, _, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y,
    )

    X_test_scaled = scaler.transform(X_test)
    y_pred = model.predict(X_test_scaled)

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(
        y_test, y_pred, average="weighted", zero_division=0
    )
    recall = recall_score(
        y_test, y_pred, average="weighted", zero_division=0
    )
    f1 = f1_score(
        y_test, y_pred, average="weighted", zero_division=0
    )

    labels = sorted(set(y_test) | set(y_pred))

    print("\n" + "=" * 60)
    print("EVALUATION RESULTS")
    print("=" * 60)
    print(f"Accuracy : {accuracy:.4f} ({accuracy * 100:.2f}%)")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1-score : {f1:.4f}")

    print("\nClassification Report:")
    print(classification_report(
        y_test,
        y_pred,
        labels=labels,
        zero_division=0,
    ))

    print("Confusion Matrix:")
    cm = confusion_matrix(y_test, y_pred, labels=labels)
    print("Labels:", labels)
    print(cm)

    # Save a JSON report for GitHub / PPT use.
    report = {
        "model": "Saved ApexScout AI model",
        "dataset": str(DATASET_DIR),
        "total_samples": int(len(y)),
        "test_samples": int(len(y_test)),
        "feature_count": int(X.shape[1]),
        "accuracy": float(accuracy),
        "precision_weighted": float(precision),
        "recall_weighted": float(recall),
        "f1_weighted": float(f1),
        "classes": labels,
        "confusion_matrix": cm.tolist(),
    }

    output_path = MODEL_DIR / "evaluation_report.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print(f"\nEvaluation report saved to: {output_path}")
    print("\nEvaluation completed successfully.")


if __name__ == "__main__":
    main()
