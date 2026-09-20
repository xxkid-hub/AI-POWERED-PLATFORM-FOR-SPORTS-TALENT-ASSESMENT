"""
Unit Tests for Model Inference, Checkpoint Loading, and Prediction Schema
"""

import os
import pytest
import numpy as np
from PIL import Image

from config.settings import SPORTS_CATEGORIES
from infer import load_trained_model, predict_sports_action

@pytest.fixture
def synthetic_image():
    # Synthetic sports frame
    img = Image.new("RGB", (64, 64), color=(30, 80, 150))
    return img

def test_load_trained_model():
    model, scaler, model_type = load_trained_model()
    assert model is not None, "Trained model must be loadable"
    assert model_type in ["sklearn", "centroid"], f"Expected sklearn or centroid, got {model_type}"
    if model_type == "sklearn":
        assert scaler is not None, "Scaler must be present for sklearn model"

def test_predict_sports_action_schema(synthetic_image):
    result = predict_sports_action(synthetic_image)
    assert result["status"] == "SUCCESS"
    assert result["predicted_sport"] in SPORTS_CATEGORIES
    assert isinstance(result["confidence_percentage"], float)
    assert 0.0 <= result["confidence_percentage"] <= 100.0
    assert "probabilities" in result
    assert "action_skill" in result
    assert "key_metric" in result
    assert "overall_score" in result

def test_probabilities_distribution(synthetic_image):
    result = predict_sports_action(synthetic_image)
    probs = result["probabilities"]
    assert len(probs) == len(SPORTS_CATEGORIES)
    # Sum of probabilities should be close to 100%
    total_prob = sum(probs.values())
    assert abs(total_prob - 100.0) < 1.0, f"Probabilities must sum to ~100%, got {total_prob}"

def test_predict_sports_action_invalid_input():
    result = predict_sports_action("non_existent_file.png")
    assert result["status"] == "ERROR"
