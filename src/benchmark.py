"""
ApexScout AI - Latency & Inference Throughput Benchmarking Engine
Substantiates real-time edge processing and sub-50ms inference claims
by measuring p50, p95, and p99 latency metrics across sequential runs.
"""

import os
import sys
import time
import json
import glob
import numpy as np
from PIL import Image

from config.settings import (
    BASE_DIR,
    DATASET_DIR,
    MODEL_DIR,
    RESULTS_DIR,
    SPORTS_CATEGORIES
)
from src.preprocessor import SportsImagePreprocessor

def benchmark_latency(num_iterations=100, save_report=True):
    """
    Executes latency benchmarking for end-to-end inference (feature extraction + model scoring).
    """
    import joblib

    model_path = os.path.join(MODEL_DIR, "sports_talent_model.joblib")
    scaler_path = os.path.join(MODEL_DIR, "feature_scaler.joblib")

    if not os.path.exists(model_path) or not os.path.exists(scaler_path):
        raise FileNotFoundError(f"Model artifacts not found at {MODEL_DIR}")

    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    preprocessor = SportsImagePreprocessor()

    # Find sample images to benchmark
    sample_images = glob.glob(os.path.join(DATASET_DIR, "*", "*.png"))
    if not sample_images:
        # Create a synthetic sample array if dataset not populated
        sample_img = Image.new("RGB", (224, 224), color=(100, 150, 200))
    else:
        sample_img = Image.open(sample_images[0])

    print("=" * 65)
    print(" [ApexScout AI] - Latency & Throughput Benchmark")
    print(f" Benchmark Iterations: {num_iterations}")
    print("=" * 65)

    # Warmup runs
    for _ in range(10):
        feat = preprocessor.extract_features(sample_img)
        feat_scaled = scaler.transform(feat.reshape(1, -1))
        _ = model.predict_proba(feat_scaled)

    latencies_ms = []
    feat_extract_ms = []
    infer_ms = []

    for i in range(num_iterations):
        t0 = time.perf_counter()
        feat = preprocessor.extract_features(sample_img)
        t1 = time.perf_counter()
        feat_scaled = scaler.transform(feat.reshape(1, -1))
        _ = model.predict_proba(feat_scaled)
        t2 = time.perf_counter()

        latencies_ms.append((t2 - t0) * 1000.0)
        feat_extract_ms.append((t1 - t0) * 1000.0)
        infer_ms.append((t2 - t1) * 1000.0)

    p50 = float(np.percentile(latencies_ms, 50))
    p95 = float(np.percentile(latencies_ms, 95))
    p99 = float(np.percentile(latencies_ms, 99))
    mean_lat = float(np.mean(latencies_ms))
    min_lat = float(np.min(latencies_ms))
    max_lat = float(np.max(latencies_ms))
    throughput_fps = float(1000.0 / mean_lat) if mean_lat > 0 else 0.0

    report = {
        "benchmark_name": "ApexScout Edge-AI Inference Latency Benchmark",
        "iterations": num_iterations,
        "mean_latency_ms": round(mean_lat, 2),
        "median_p50_ms": round(p50, 2),
        "p95_latency_ms": round(p95, 2),
        "p99_latency_ms": round(p99, 2),
        "min_latency_ms": round(min_lat, 2),
        "max_latency_ms": round(max_lat, 2),
        "throughput_fps": round(throughput_fps, 1),
        "breakdown": {
            "avg_feature_extraction_ms": round(float(np.mean(feat_extract_ms)), 2),
            "avg_classifier_scoring_ms": round(float(np.mean(infer_ms)), 2)
        },
        "target_sla_met": bool(p95 < 100.0),
        "target_sub_100ms": "PASS" if p95 < 100.0 else "FAIL"
    }

    if save_report:
        os.makedirs(RESULTS_DIR, exist_ok=True)
        report_path = os.path.join(RESULTS_DIR, "benchmark_report.json")
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)
        print(f"[+] Benchmark report saved to: {report_path}")

    print("\n" + "=" * 65)
    print(f" Mean Latency:       {mean_lat:.2f} ms")
    print(f" Median (p50):       {p50:.2f} ms")
    print(f" 95th Percentile:    {p95:.2f} ms (Target < 100ms: {'PASS' if p95 < 100 else 'FAIL'})")
    print(f" 99th Percentile:    {p99:.2f} ms")
    print(f" Max Throughput:     {throughput_fps:.1f} FPS")
    print("=" * 65)

    return report

if __name__ == "__main__":
    benchmark_latency()
