"""
ApexScout AI - Central Configuration & Schema Definition
Provides global paths, hyperparameters, categories, and settings loader.
"""

import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASET_DIR = os.path.join(BASE_DIR, "dataset")
DATASETS_DIR = os.path.join(BASE_DIR, "datasets")
MODEL_DIR = os.path.join(BASE_DIR, "trained_model")
RESULTS_DIR = os.path.join(BASE_DIR, "results")
CONFIG_DIR = os.path.join(BASE_DIR, "config")

os.makedirs(MODEL_DIR, exist_ok=True)
os.makedirs(RESULTS_DIR, exist_ok=True)

# Standardized Sports Categories (6 Core Classes)
SPORTS_CATEGORIES = [
    "Athletics",
    "Basketball",
    "Cricket",
    "Kabaddi",
    "Soccer",
    "Volleyball"
]

IMG_TARGET_SIZE = (48, 48)
DEFAULT_SEED = 42
TEST_SPLIT = 0.20

# Biomechanical Skill and Kinematic Telemetry Mapping
SKILL_MAPPING = {
    "Athletics": {
        "skill": "Explosive High Jump & Vertical Leap",
        "category": "Explosiveness & High Jump",
        "key_metric": "Takeoff Velocity: 4.35 m/s | Apex: 36.8 in",
        "plant_foot_expected": "Penultimate foot plant (118° preload)",
        "ideal_balance_score": 96
    },
    "Basketball": {
        "skill": "Crossover to 3-Point Jump Shot",
        "category": "Ball Handling & Shooting Arc",
        "key_metric": "Release Velocity: 28.0 km/h | Arc: 48° Entry",
        "plant_foot_expected": "Square 1-2 plant step",
        "ideal_balance_score": 93
    },
    "Cricket": {
        "skill": "Outswinger Fast Bowling Action",
        "category": "Pace Bowling & Seam Release",
        "key_metric": "Release Speed: 138.6 km/h | 2.4° Outswing",
        "plant_foot_expected": "Front foot braced (178° lockout)",
        "ideal_balance_score": 96
    },
    "Kabaddi": {
        "skill": "Toe Touch & Low-Squat Dubki Raid",
        "category": "Raiding & Agility",
        "key_metric": "Burst Speed: 22.4 km/h | Reaction: 0.38s",
        "plant_foot_expected": "Low center of gravity (45° flex)",
        "ideal_balance_score": 95
    },
    "Soccer": {
        "skill": "Precision Penalty Strike & Placement",
        "category": "Shooting & Striking",
        "key_metric": "Shot Speed: 91.0 km/h | 14 rad/s Curve",
        "plant_foot_expected": "Good (35° ankle angle, 12cm lateral spacing)",
        "ideal_balance_score": 94
    },
    "Volleyball": {
        "skill": "Power Cross-Court Aerial Spike",
        "category": "Aerial Attack & Placement",
        "key_metric": "Spike Speed: 88.5 km/h | Angle: -28° Topspin",
        "plant_foot_expected": "Dynamic block step conversion",
        "ideal_balance_score": 92
    }
}

DEFAULT_HYPERPARAMS = {
    "seed": DEFAULT_SEED,
    "test_split": TEST_SPLIT,
    "target_size": list(IMG_TARGET_SIZE),
    "model": {
        "rf_n_estimators": 100,
        "rf_max_depth": 10,
        "et_n_estimators": 100,
        "et_max_depth": 10,
        "voting": "soft"
    },
    "augmentation": {
        "target_samples_per_sport": 100,
        "flip_prob": 0.4,
        "max_rotation_deg": 18.0
    }
}

def get_config(config_path=None):
    """
    Loads configuration from YAML or JSON if available, falling back to defaults.
    """
    if config_path is None:
        yaml_path = os.path.join(CONFIG_DIR, "config.yaml")
        json_path = os.path.join(CONFIG_DIR, "config.json")
        if os.path.exists(yaml_path):
            config_path = yaml_path
        elif os.path.exists(json_path):
            config_path = json_path

    config = dict(DEFAULT_HYPERPARAMS)

    if config_path and os.path.exists(config_path):
        try:
            if config_path.endswith((".yaml", ".yml")):
                try:
                    import yaml
                    with open(config_path, "r", encoding="utf-8") as f:
                        loaded = yaml.safe_load(f)
                        if isinstance(loaded, dict):
                            config.update(loaded)
                except ImportError:
                    pass
            elif config_path.endswith(".json"):
                with open(config_path, "r", encoding="utf-8") as f:
                    loaded = json.load(f)
                    if isinstance(loaded, dict):
                        config.update(loaded)
        except Exception as e:
            print(f"[!] Warning: Could not parse config file {config_path}: {e}")

    return config
