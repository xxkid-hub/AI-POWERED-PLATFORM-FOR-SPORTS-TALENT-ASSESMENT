#!/usr/bin/env python3
"""
ApexScout AI - Multi-Sport Model Training CLI Pipeline
Trains a custom Machine Learning & Kinematic Feature Model directly on the dataset/ directory
across Athletics, Basketball, Cricket, Kabaddi, Soccer, and Volleyball.
Supports CLI arguments (--seed, --config, --data-dir, --model-dir) for full reproducibility.
"""

import os
import sys
import argparse

# Ensure UTF-8 output encoding on Windows stdout
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from config.settings import (
    DATASET_DIR,
    MODEL_DIR,
    SPORTS_CATEGORIES,
    DEFAULT_SEED,
    TEST_SPLIT,
    get_config
)
from src.preprocessor import extract_features_from_image, SportsImagePreprocessor
from src.trainer import SportsModelTrainer, seed_everything

def train_and_evaluate(
    data_dir=DATASET_DIR,
    model_dir=MODEL_DIR,
    config_path=None,
    seed=DEFAULT_SEED,
    test_split=TEST_SPLIT,
    n_estimators=100,
    max_depth=10
):
    """
    Main training execution function (compatible with existing code and automated evaluators).
    """
    cfg = get_config(config_path)
    trainer = SportsModelTrainer(
        data_dir=data_dir,
        model_dir=model_dir,
        config=cfg,
        seed=seed
    )
    return trainer.train(
        test_size=test_split,
        n_estimators_rf=n_estimators,
        n_estimators_et=n_estimators,
        max_depth=max_depth
    )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="ApexScout AI - Multi-Sport ML Training CLI Pipeline"
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=DEFAULT_SEED,
        help="Random seed for reproducible training (default: 42)"
    )
    parser.add_argument(
        "--config",
        type=str,
        default=None,
        help="Path to external YAML or JSON configuration file"
    )
    parser.add_argument(
        "--data-dir",
        type=str,
        default=DATASET_DIR,
        help=f"Path to dataset directory (default: {DATASET_DIR})"
    )
    parser.add_argument(
        "--model-dir",
        type=str,
        default=MODEL_DIR,
        help=f"Output directory for trained model artifacts (default: {MODEL_DIR})"
    )
    parser.add_argument(
        "--test-split",
        type=float,
        default=TEST_SPLIT,
        help="Ratio for holdout test split (default: 0.20)"
    )
    parser.add_argument(
        "--n-estimators",
        type=int,
        default=100,
        help="Number of decision trees for ensemble estimators (default: 100)"
    )
    parser.add_argument(
        "--max-depth",
        type=int,
        default=10,
        help="Maximum tree depth (default: 10)"
    )

    args = parser.parse_args()
    train_and_evaluate(
        data_dir=args.data_dir,
        model_dir=args.model_dir,
        config_path=args.config,
        seed=args.seed,
        test_split=args.test_split,
        n_estimators=args.n_estimators,
        max_depth=args.max_depth
    )
