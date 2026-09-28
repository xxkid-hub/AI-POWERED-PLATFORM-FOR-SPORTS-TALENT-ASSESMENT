"""
ApexScout AI - Weekly AI Training & Progression Arena Tab
Renders automated kinetic deficiency breakdowns, 7-day training regimens,
multi-athlete progression trajectory charts, and head-to-head peer duels.
"""

import streamlit as st
import pandas as pd
from src.ui.mock_data import TRAINING_DEFICIENCIES, WEEKLY_SCHEDULE


def render_progression_tab():
    st.title("Weekly AI Training Loops & Peer Progression Arena")
    st.markdown("Automated kinetic deficiency breakdown, 7-day corrective training regimen, multi-athlete trajectory graphs, and side-by-side skeletal duels.")

    col_t1, col_t2 = st.columns([1.2, 1])

    with col_t1:
        st.markdown("### **Automated Kinetic Deficiency Breakdown**")
        for def_item in TRAINING_DEFICIENCIES:
            with st.expander(f"{def_item['title']} — {def_item['severity']}", expanded=True):
                st.markdown(f"**Impact:** {def_item['impact']}")
                st.code(def_item['trace'], language="text")
                st.markdown(f"**AI Prescribed Drill:** `{def_item['drill']}`")

    with col_t2:
        st.markdown("### **7-Day AI Corrective Plan (Week 4)**")
        for day, focus, drill in WEEKLY_SCHEDULE:
            st.markdown(f"**{day}**: `{focus}`<br/><small style='color:#94A3B8;'>{drill}</small>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### **Multi-Athlete Peer Progression Trajectory Curves (Weeks 1 to 8)**")

    chart_metric = st.selectbox("Select Progression Metric", ["Vertical Jump (inches)", "Dribble Cadence (Hz)", "40-Yard Sprint Time (sec)", "Kinetic Symmetry Index (%)"])

    weeks = [f"W{i}" for i in range(1, 9)]
    if chart_metric == "Vertical Jump (inches)":
        df_chart = pd.DataFrame({
            "Weeks": weeks,
            "You (Alex Rivera)": [31.2, 32.5, 34.0, 36.4, 37.1, 37.8, 38.4, 39.0],
            "Peer Average": [28.5, 29.2, 30.0, 31.0, 31.8, 32.4, 33.0, 33.6],
            "Elite Benchmark": [36.0, 36.5, 37.0, 37.5, 38.0, 38.5, 39.0, 39.5]
        }).set_index("Weeks")
    elif chart_metric == "Dribble Cadence (Hz)":
        df_chart = pd.DataFrame({
            "Weeks": weeks,
            "You (Alex Rivera)": [3.6, 3.9, 4.2, 4.8, 5.0, 5.2, 5.3, 5.5],
            "Peer Average": [3.2, 3.4, 3.6, 3.8, 4.0, 4.1, 4.2, 4.3],
            "Elite Benchmark": [4.5, 4.7, 4.8, 5.0, 5.2, 5.3, 5.5, 5.6]
        }).set_index("Weeks")
    elif chart_metric == "40-Yard Sprint Time (sec)":
        df_chart = pd.DataFrame({
            "Weeks": weeks,
            "You (Alex Rivera)": [4.82, 4.71, 4.58, 4.42, 4.38, 4.34, 4.30, 4.28],
            "Peer Average": [5.10, 5.02, 4.95, 4.88, 4.80, 4.75, 4.70, 4.65],
            "Elite Benchmark": [4.45, 4.40, 4.36, 4.32, 4.28, 4.25, 4.22, 4.20]
        }).set_index("Weeks")
    else:
        df_chart = pd.DataFrame({
            "Weeks": weeks,
            "You (Alex Rivera)": [78, 82, 88, 94, 95, 97, 98, 99],
            "Peer Average": [72, 74, 76, 80, 82, 84, 85, 87],
            "Elite Benchmark": [92, 94, 95, 96, 97, 98, 99, 100]
        }).set_index("Weeks")

    st.line_chart(df_chart)

    st.markdown("---")
    st.markdown("### **Head-to-Head Drill Duel Arena (Side-by-Side Skeletons)**")
    
    col_d1, col_d2 = st.columns([1, 2])
    with col_d1:
        duel_peer = st.selectbox("Select Peer Competitor", ["Mateo Silva (Soccer - 91 km/h)", "Ravi Kumar (Kabaddi - 22.4 km/h)", "Simran Preet (Cricket - 138.6 km/h)"])
        st.markdown("**Drill Type:** `Max Vertical Jump Showdown`")
        if st.button("Launch Head-to-Head Skeletal Duel", type="primary", use_container_width=True):
            st.success("DUEL OUTCOME: You won the showdown against Mateo Silva with +1.4 inches higher apex elevation!")
    
    with col_d2:
        st.markdown("""
        <div class='card-box' style='text-align:center;'>
            <h4 style='color:#00F2FE;'>You (Alex Rivera) 36.4" Apex VS Mateo Silva 31.5" Apex</h4>
            <p style='font-size:0.85rem;color:#94A3B8;'>Side-by-side skeletal kinematic overlay rendered in real-time combine.</p>
        </div>
        """, unsafe_allow_html=True)
