#!/usr/bin/env python3
"""
ApexScout AI - Server CLI Entrypoint (Streamlit Platform)
Launches the full interactive sports talent assessment platform on Streamlit port 8501.
"""

import sys
import os
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

DEFAULT_STREAMLIT_PORT = 8501


def run_streamlit_app(port: int = DEFAULT_STREAMLIT_PORT):
    """Launches the Streamlit application on the designated port."""
    app_path = os.path.join(BASE_DIR, "streamlit_app.py")
    cmd = [
        sys.executable,
        "-m",
        "streamlit",
        "run",
        app_path,
        "--server.port",
        str(port),
        "--server.headless",
        "true",
        "--browser.serverAddress",
        "localhost",
    ]
    print("=" * 70, flush=True)
    print(" [ApexScout AI] STREAMLIT PLATFORM SERVER", flush=True)
    print("=" * 70, flush=True)
    print(f"  * Serving at: http://localhost:{port}", flush=True)
    print("=" * 70, flush=True)
    try:
        subprocess.run(cmd, check=True)
    except KeyboardInterrupt:
        print("\n[*] Streamlit server stopped.", flush=True)


if __name__ == '__main__':
    port = DEFAULT_STREAMLIT_PORT
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        port = int(sys.argv[1])
    run_streamlit_app(port=port)
