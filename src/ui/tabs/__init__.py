"""
ApexScout AI - UI Tabs Package
Modular tab renderers for Streamlit frontend.
"""

from .combine import render_combine_tab
from .medical import render_medical_tab
from .ml_hub import render_ml_hub_tab

__all__ = [
    "render_combine_tab",
    "render_medical_tab",
    "render_ml_hub_tab",
]
