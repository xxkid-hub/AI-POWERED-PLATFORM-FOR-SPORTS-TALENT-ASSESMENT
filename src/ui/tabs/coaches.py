"""
ApexScout AI - Coaches & Scouts Marketplace Tab
Renders certified scout profiles, direct messaging, and digital dossier dispatching.
"""

import streamlit as st
from src.ui.mock_data import COACH_DIRECTORY


def render_coaches_tab():
    st.title("Certified Coaches & Grassroots Scout Portal")
    st.markdown("Connect directly with verified collegiate scouts, UEFA/NBA development directors, and Olympic performance coaches.")

    for c in COACH_DIRECTORY:
        with st.container():
            st.markdown(f"""
            <div class='card-box'>
                <h3>{c['name']} <span style='font-size:0.85rem;color:#00F2FE;'>• {c['role']}</span></h3>
                <p style='color:#94A3B8;'>Sport: <strong>{c['sport']}</strong> | Location: <strong>{c['loc']}</strong> | Combine Fee: <span style='color:#39FF14;'>{c['fee']}</span></p>
            </div>
            """, unsafe_allow_html=True)
            col_b1, col_b2 = st.columns(2)
            with col_b1:
                if st.button(f"Direct Message {c['name']}", key=f"msg_{c['name']}"):
                    st.info(f"Opening encrypted chat with {c['name']}...")
            with col_b2:
                if st.button(f"Dispatch Verified Dossier to {c['name']}", key=f"dos_{c['name']}"):
                    st.success(f"✓ Official Dossier (12-component telemetry + 48h medical token) dispatched to {c['name']}!")
