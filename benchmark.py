#!/usr/bin/env python3
"""
ApexScout AI - Latency Benchmarking CLI
Measures end-to-end inference latency (p50, p95, p99) and verifies sub-50ms execution.
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

from src.benchmark import benchmark_latency

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ApexScout AI - Latency Benchmarking CLI")
    parser.add_argument("--iterations", type=int, default=100, help="Number of benchmark iterations (default: 100)")
    args = parser.parse_args()

    benchmark_latency(num_iterations=args.iterations, save_report=True)
