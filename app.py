"""
ApexScout AI - Official Application Entrypoint (Streamlit)
Executes the comprehensive Next-Gen AI Vision Sports Ecosystem.
"""

import os
import runpy

if __name__ == "__main__" or "__file__" in globals():
    app_target = os.path.join(os.path.dirname(os.path.abspath(__file__)), "streamlit_app.py")
    runpy.run_path(app_target, run_name="__main__")
