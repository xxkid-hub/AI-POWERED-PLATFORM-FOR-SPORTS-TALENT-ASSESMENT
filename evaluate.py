#!/usr/bin/env python3
"""
ApexScout AI - Standalone Evaluation CLI
Evaluates the trained model against hold-out splits without re-training,
generating visual confusion matrices and evaluation metrics in results/.
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

from config.settings import DATASET_DIR, MODEL_DIR, RESULTS_DIR, DEFAULT_SEED, TEST_SPLIT
from src.evaluate import evaluate_model

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ApexScout AI - Model Evaluation CLI")
    parser.add_argument("--data-dir", type=str, default=DATASET_DIR, help="Path to dataset directory")
    parser.add_argument("--model-dir", type=str, default=MODEL_DIR, help="Path to trained model directory")
    parser.add_argument("--results-dir", type=str, default=RESULTS_DIR, help="Path to save evaluation artifacts")
    parser.add_argument("--test-split", type=float, default=TEST_SPLIT, help="Holdout split ratio")
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED, help="Random seed for reproducible evaluation split")

    args = parser.parse_args()
    evaluate_model(
        data_dir=args.data_dir,
        model_dir=args.model_dir,
        results_dir=args.results_dir,
        test_size=args.test_split,
        seed=args.seed
    )
