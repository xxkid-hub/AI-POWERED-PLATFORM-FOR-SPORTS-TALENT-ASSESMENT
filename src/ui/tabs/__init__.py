"""
ApexScout AI - UI Tabs Package
Modular tab renderers for Streamlit frontend.
"""

from .combine import render_combine_tab
from .medical import render_medical_tab
from .ml_hub import render_ml_hub_tab
from .progression import render_progression_tab
from .scouting import render_leaderboard_tab, render_passport_tab
from .coaches import render_coaches_tab
from .helpline import render_helpline_tab

__all__ = [
    "render_combine_tab",
    "render_medical_tab",
    "render_ml_hub_tab",
    "render_progression_tab",
    "render_leaderboard_tab",
    "render_passport_tab",
    "render_coaches_tab",
    "render_helpline_tab",
]
