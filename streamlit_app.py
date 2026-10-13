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
# PAGE CONFIGURATION (Clean, professional, emoji-free)
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="ApexScout AI | Sports Talent Assessment",
    layout="wide",
    initial_sidebar_state="expanded"
)

from src.ui.i18n import t

# Inject custom athletic sports-tech CSS
inject_custom_styles()

# -----------------------------------------------------------------------------
# SIDEBAR NAVIGATION & GRASSROOTS SUITE
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("### **Rural & Grassroots Suite**")
    language = st.selectbox(
        "Language / भाषा",
        ["English", "हिन्दी (Hindi)", "Español"],
        index=0,
        key="app_language"
    )

    low_data_mode = st.toggle(t("low_data_mode", language), value=False)
    if low_data_mode:
        st.caption(t("low_data_active", language))

    st.divider()
    st.markdown(f"## **{t('sidebar_title', language)}**")
    st.caption(t("sidebar_tagline", language))
    st.divider()

    nav_options = [
        "Video & AR Combine Analysis",
        "Custom ML Model & Dataset Hub",
        "24–48h Medical SLA & OCR",
        "Weekly AI Training & Peer Duels",
        "Verified Scout Leaderboard",
        "Coaches & Scouts Marketplace",
        "24/7 Helpline & Sports Physio",
        "Verifiable Digital Passport"
    ]

    nav_labels = {
        "Video & AR Combine Analysis": t("nav_combine", language),
        "Custom ML Model & Dataset Hub": t("nav_ml_hub", language),
        "24–48h Medical SLA & OCR": t("nav_medical", language),
        "Weekly AI Training & Peer Duels": t("nav_progression", language),
        "Verified Scout Leaderboard": t("nav_leaderboard", language),
        "Coaches & Scouts Marketplace": t("nav_coaches", language),
        "24/7 Helpline & Sports Physio": t("nav_helpline", language),
        "Verifiable Digital Passport": t("nav_passport", language),
    }

    nav_choice = st.radio(
        "Navigation",
        nav_options,
        format_func=lambda x: f"{nav_labels.get(x, x)}" if "english" not in language.lower() else x,
        index=0
    )

    st.markdown("---")
    st.caption(t("logged_in_as", language))

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
    render_leaderboard_tab(language=language)

elif nav_choice == "Coaches & Scouts Marketplace":
    render_coaches_tab(language=language)

elif nav_choice == "24/7 Helpline & Sports Physio":
    render_helpline_tab(language=language)

elif nav_choice == "Verifiable Digital Passport":
    render_passport_tab(language=language)

