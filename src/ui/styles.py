"""
ApexScout AI - UI Styles & Athletic Design System
Custom CSS tokens, typography, dark carbon theme, and glassmorphic HUD styling.
"""

import streamlit as st


SPORTS_TECH_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800;900&family=Inter:wght@400;500;600;700&display=swap');

    /* Dark Carbon Background & Neon Cyan / Lime Accents */
    .stApp {
        background-color: #080B11;
        color: #F8FAFC;
        font-family: 'Inter', sans-serif;
    }
    
    /* Metrics Card Styling */
    div[data-testid="stMetricValue"] {
        font-family: 'Outfit', sans-serif;
        font-weight: 800;
        color: #00F2FE;
    }
    
    /* Custom Headers */
    h1, h2, h3 {
        font-family: 'Outfit', sans-serif;
        font-weight: 700;
        letter-spacing: -0.02em;
    }
    
    /* Table Styling matching PRD design */
    .skill-table-header {
        font-size: 1.15rem;
        font-weight: 800;
        text-transform: uppercase;
        color: #A0AEC0;
        letter-spacing: 0.05em;
        border-bottom: 2px solid rgba(0, 242, 254, 0.3);
        padding-bottom: 0.5rem;
        margin-bottom: 1rem;
    }
    
    .status-badge-green {
        background-color: rgba(57, 255, 20, 0.15);
        color: #39FF14;
        border: 1px solid #39FF14;
        padding: 4px 10px;
        border-radius: 9999px;
        font-weight: 700;
        font-size: 0.85rem;
        display: inline-block;
    }
    
    .status-badge-yellow {
        background-color: rgba(255, 184, 0, 0.15);
        color: #FFB800;
        border: 1px solid #FFB800;
        padding: 4px 10px;
        border-radius: 9999px;
        font-weight: 700;
        font-size: 0.85rem;
        display: inline-block;
    }
    
    .status-badge-red {
        background-color: rgba(255, 0, 85, 0.15);
        color: #FF0055;
        border: 1px solid #FF0055;
        padding: 4px 10px;
        border-radius: 9999px;
        font-weight: 700;
        font-size: 0.85rem;
        display: inline-block;
    }
    
    .hud-box {
        background: rgba(15, 23, 42, 0.7);
        border: 1px solid rgba(0, 242, 254, 0.2);
        border-radius: 12px;
        padding: 1.25rem;
        backdrop-filter: blur(8px);
        margin-bottom: 1rem;
    }
    
    .hud-header {
        color: #00F2FE;
        font-size: 0.85rem;
        font-weight: 800;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        margin-bottom: 0.5rem;
    }
</style>
"""


def inject_custom_styles():
    """Injects high-performance CSS styles into the Streamlit DOM."""
    st.markdown(SPORTS_TECH_CSS, unsafe_allow_html=True)


def render_brand_header():
    """Renders the top title and branding badges."""
    st.title("⚡ ApexScout AI — Next-Gen AI Vision Sports Ecosystem")
    st.caption("Real-Time Kinematics • FFT Deepfake Guard • 24–48h Medical SLA • Weekly Training Loops • P2P Progression Arena")
