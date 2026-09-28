"""
ApexScout AI - Next-Gen AI Vision Sports Ecosystem (Streamlit Frontend)
Vision-first sports scouting, biomechanical analysis, and progression ecosystem.
Modular orchestrator delegating to specialized presentation tabs.
"""

import sys
import os

# Guarantee project root is in sys.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

import streamlit as st
from src.ui.styles import inject_custom_styles, render_brand_header
from src.ui.tabs import (
    render_combine_tab,
    render_medical_tab,
    render_ml_hub_tab,
    render_progression_tab,
    render_leaderboard_tab,
    render_passport_tab,
    render_coaches_tab,
    render_helpline_tab,
)

# -----------------------------------------------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="ApexScout AI | Sports Talent Assessment",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject custom athletic sports-tech CSS
inject_custom_styles()

# -----------------------------------------------------------------------------
# SIDEBAR NAVIGATION & GRASSROOTS SUITE
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("## ⚡ **ApexScout AI**")
    st.caption("Vision-First Sports Scouting Ecosystem")
    st.divider()

    nav_choice = st.radio(
        "Navigation",
        [
            "Video & AR Combine Analysis",
            "Custom ML Model & Dataset Hub",
            "24–48h Medical SLA & OCR",
            "Weekly AI Training & Peer Duels",
            "Verified Scout Leaderboard",
            "Coaches & Scouts Marketplace",
            "24/7 Helpline & Sports Physio",
            "Verifiable Digital Passport"
        ],
        index=0
    )

    st.divider()
    st.markdown("### **Rural & Grassroots Suite**")
    language = st.selectbox("Language / भाषा", ["English", "हिन्दी (Hindi)", "Español"])
    low_data_mode = st.toggle("Low-Data Mode (<120 KB)", value=False)
    if low_data_mode:
        st.caption("✓ Video telemetry compressed for rural cellular networks.")
    
    st.markdown("---")
    st.caption("Logged in as: **Alex Rivera (Athlete)**")

# -----------------------------------------------------------------------------
# ROUTER: DISPATCH TO MODULAR TABS
# -----------------------------------------------------------------------------
if nav_choice == "Video & AR Combine Analysis":
    render_combine_tab()

elif nav_choice == "Custom ML Model & Dataset Hub":
    render_ml_hub_tab()

elif nav_choice == "24–48h Medical SLA & OCR":
    render_medical_tab()

elif nav_choice == "Weekly AI Training & Peer Duels":
    render_progression_tab()

elif nav_choice == "Verified Scout Leaderboard":
    render_leaderboard_tab()

elif nav_choice == "Coaches & Scouts Marketplace":
    render_coaches_tab()

elif nav_choice == "24/7 Helpline & Sports Physio":
    render_helpline_tab(language=language)

elif nav_choice == "Verifiable Digital Passport":
    render_passport_tab()
