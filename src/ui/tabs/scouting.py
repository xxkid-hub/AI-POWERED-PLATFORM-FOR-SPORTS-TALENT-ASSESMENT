"""
ApexScout AI - Verified Scout Leaderboard & Digital Passport Tabs
Renders the global talent rankings and verifiable digital athlete passports with JSON download.
"""

import json
from datetime import datetime
import streamlit as st
import pandas as pd
from src.ui.mock_data import LEADERBOARD_RECORDS


def render_leaderboard_tab():
    st.title("Verified Grassroots & Elite Leaderboard")
    st.markdown("Global rankings of top talent with verified 12-component biomechanics and **24–48h Medical SLA badges**.")

    df_lead = pd.DataFrame(LEADERBOARD_RECORDS)
    st.dataframe(df_lead, use_container_width=True)


def render_passport_tab():
    st.title("Verifiable Digital Athlete Passport")
    st.markdown("Official scout combine dossier with tamper-proof video telemetry, 24-48h medical clearance token, and kinetic skill matrix.")

    st.markdown("""
    <div class='card-box' style='border:2px solid #00F2FE;'>
        <h2>Alex Rivera</h2>
        <p style='color:#00F2FE;font-weight:700;'>Football / Soccer • Penalty Striker & Winger</p>
        <p style='color:#94A3B8;'>Age 18 • 5'11" (180 cm) • Grassroots Combine Athlete</p>
        <hr style='border-color:rgba(255,255,255,0.08);'/>
        <div style='display:flex;justify-content:space-between;flex-wrap:wrap;'>
            <div><strong>Top Shot Speed:</strong> 91.0 km/h</div>
            <div><strong>Accuracy:</strong> 92%</div>
            <div><strong>Reaction Time:</strong> 0.82 sec</div>
            <div><strong>SLA Status:</strong> <span style='color:#39FF14;'>✓ 24-48h Verified</span></div>
        </div>
        <hr style='border-color:rgba(255,255,255,0.08);'/>
        <div style='display:flex;justify-content:space-between;align-items:center;'>
            <span style='font-size:1.8rem;font-weight:900;color:#39FF14;'>Combine Rating: 94/100</span>
            <code>TOKEN: APEX-VERIFIED-RURAL-2026-8942</code>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.download_button(
        label="Download Official JSON Passport Dossier",
        data=json.dumps({
            "athlete": "Alex Rivera",
            "sport": "Football / Soccer",
            "combine_rating": 94,
            "shot_speed": "91 km/h",
            "accuracy": "92%",
            "medical_sla_status": "VERIFIED_24H",
            "deepfake_forensics": "PASSED_CLEAN",
            "issued_at": datetime.now().isoformat()
        }, indent=2),
        file_name="Alex_Rivera_ApexScout_Passport.json",
        mime="application/json"
    )
