"""
End-to-End Pipeline Sanity & Integration Tests
"""

import os
import glob
import pytest
from config.settings import get_config, SPORTS_CATEGORIES, DATASET_DIR
from infer import predict_sports_action

def test_config_loader():
    cfg = get_config()
    assert isinstance(cfg, dict)
    assert "data" in cfg or "model" in cfg or "seed" in cfg

def test_inference_on_real_samples():
    for sport in SPORTS_CATEGORIES:
        sport_dir = os.path.join(DATASET_DIR, sport)
        images = glob.glob(os.path.join(sport_dir, "*.png"))
        if images:
            sample_img = images[0]
            result = predict_sports_action(sample_img)
            assert result["status"] == "SUCCESS"
            assert result["predicted_sport"] in SPORTS_CATEGORIES
            assert result["confidence_percentage"] > 0
