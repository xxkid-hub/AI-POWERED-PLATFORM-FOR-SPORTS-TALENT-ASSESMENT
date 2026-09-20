"""
Unit Tests for Model Inference, Checkpoint Loading, and Prediction Schema
Includes tests for athletic motion validation and rejection of static non-sports frames.
"""

import os
import glob
import pytest
import numpy as np
from PIL import Image

from config.settings import SPORTS_CATEGORIES, DATASET_DIR
from infer import load_trained_model, predict_sports_action

@pytest.fixture
def athletic_sample_image():
    # Load a real sports image from dataset if available, or generate patterned image
    sample_files = glob.glob(os.path.join(DATASET_DIR, "*", "*.png"))
    if sample_files:
        return Image.open(sample_files[0])
    
    # Fallback to gradient pattern with edges
    arr = np.zeros((100, 100, 3), dtype=np.uint8)
    arr[20:80, 30:70] = 200
    arr[40:60, 10:90] = 180
    return Image.fromarray(arr)

@pytest.fixture
def static_blank_image():
    # Flat solid color (no motion/action contrast)
    return Image.new("RGB", (64, 64), color=(200, 200, 200))

def test_load_trained_model():
    model, scaler, model_type = load_trained_model()
    assert model is not None, "Trained model must be loadable"
    assert model_type in ["sklearn", "centroid"], f"Expected sklearn or centroid, got {model_type}"
    if model_type == "sklearn":
        assert scaler is not None, "Scaler must be present for sklearn model"

def test_predict_sports_action_schema(athletic_sample_image):
    result = predict_sports_action(athletic_sample_image)
    assert result["status"] == "SUCCESS"
    assert result["predicted_sport"] in SPORTS_CATEGORIES
    assert isinstance(result["confidence_percentage"], float)
    assert 0.0 <= result["confidence_percentage"] <= 100.0
    assert "probabilities" in result
    assert "action_skill" in result
    assert "key_metric" in result
    assert "overall_score" in result

def test_probabilities_distribution(athletic_sample_image):
    result = predict_sports_action(athletic_sample_image)
    probs = result["probabilities"]
    assert len(probs) == len(SPORTS_CATEGORIES)
    # Sum of probabilities should be close to 100%
    total_prob = sum(probs.values())
    assert abs(total_prob - 100.0) < 1.0, f"Probabilities must sum to ~100%, got {total_prob}"

def test_rejection_of_no_motion_static_image(static_blank_image):
    result = predict_sports_action(static_blank_image)
    assert result["status"] == "ERROR"
    assert result["error_code"] == "NO_SPORTS_MOTION"
    assert "NO SPORTS" in result["message"]

def test_predict_sports_action_invalid_input():
    result = predict_sports_action("non_existent_file.png")
    assert result["status"] == "ERROR"
