"""
ApexScout AI - UI Tabs Package
Modular tab renderers for Streamlit frontend.
"""

from .combine import render_combine_tab
from .medical import render_medical_tab

__all__ = [
    "render_combine_tab",
    "render_medical_tab",
]
