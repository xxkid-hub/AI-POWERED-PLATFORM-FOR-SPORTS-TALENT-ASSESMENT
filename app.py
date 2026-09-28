"""
ApexScout AI - Official Application Entrypoint (Streamlit)
Executes the comprehensive Next-Gen AI Vision Sports Ecosystem.
"""

import sys
import os
import runpy

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

if __name__ == "__main__" or "__file__" in globals():
    app_target = os.path.join(BASE_DIR, "streamlit_app.py")
    runpy.run_path(app_target, run_name="__main__")
