#!/usr/bin/env python3
"""
ApexScout AI - Local Web & API Server CLI Entrypoint
Serves the static web application and provides RESTful endpoints for sports AI assessment,
medical 24h compliance verification, coach discovery, and helpline ticket submission.
"""

import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from src.server import run_server, DEFAULT_PORT

if __name__ == '__main__':
    port = DEFAULT_PORT
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        port = int(sys.argv[1])
    run_server(port=port)
