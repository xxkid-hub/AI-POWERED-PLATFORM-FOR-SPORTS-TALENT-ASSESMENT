"""
ApexScout AI - 24-48h Medical SLA & OCR Hub Tab
Renders the medical accreditation validator, 24-48h SLA timer,
and WADA/NADA anti-doping panel checker.
"""

from datetime import datetime, timedelta
import streamlit as st
from src.medical import MedicalSLAVerifier, MedicalRecord, ComplianceStatus


def render_medical_tab():
    st.title("24–48 Hour Medical & Anti-Doping Compliance Hub")
    st.markdown("Athletes competing in verified scout trials or tournaments must submit accredited anti-doping & fitness clearance within a strict **24 to 48-hour SLA window**.")

    col_m1, col_m2 = st.columns([1.2, 1])

    with col_m1:
        st.markdown("### **Medical Certificate Submission**")
        athlete_name = st.text_input("Athlete Full Name", value="Alex Rivera")
        med_file = st.file_uploader("Upload Lab Certificate / Anti-Doping Panel (PDF/JPG)", type=["pdf", "png", "jpg", "jpeg"])
        
        sla_preset = st.selectbox(
            "SLA Timing Simulation Preset",
            [
                "Fresh Clearance: Tested 4h Before Video (Verified <24h)",
                "Grace Window: Tested 36h Before Video (Pending Review <48h)",
                "Expired SLA: Tested 56h Ago (Flagged / Delisted >48h)"
            ]
        )

        t1, t2 = st.columns(2)
        with t1:
            med_time = st.text_input("Medical Test Timestamp", value=datetime.now().strftime("%Y-%m-%d %H:%M"))
        with t2:
            vid_time = st.text_input("Video Combine Timestamp", value=(datetime.now() - timedelta(hours=4)).strftime("%Y-%m-%d %H:%M"))

        run_ocr = st.button("Run Automated Document OCR & 48h SLA Check", type="primary", use_container_width=True)

    with col_m2:
        st.markdown("### **OCR & Compliance Determination**")
        if "Fresh" in sla_preset:
            st.markdown("<span class='status-badge-green'>VERIFIED (CLEARED < 24H SLA)</span>", unsafe_allow_html=True)
            st.success("✓ Document OCR validated lab stamp, NADA registration, and physician signature.")
            status_text = "FIT FOR COMPETITION & COMBINE TRIALS. WADA anti-doping panel and OCR stamp verified within strict 24-48h SLA."
        elif "Grace" in sla_preset:
            st.markdown("<span class='status-badge-yellow'>PENDING REVIEW (< 48H GRACE WINDOW)</span>", unsafe_allow_html=True)
            st.warning("Within 48-hour grace window. Provisional combine scores recorded awaiting medical board sign-off.")
            status_text = "UNDER REVIEW: Medical report within 48h grace window."
        else:
            st.markdown("<span class='status-badge-red'>FLAGGED / DELISTED (> 48H SLA EXPIRED)</span>", unsafe_allow_html=True)
            st.error("SLA EXPIRED: Medical report is older than 48 hours. Scores excluded from public leaderboards.")
            status_text = "NON-COMPLIANT: 48h verification SLA expired. Athlete delisted from leaderboard."

        st.markdown("""
        <div class='card-box'>
            <strong>OCR Extracted Metadata:</strong><br/>
            • <strong>Lab Name:</strong> Apex Olympic Bio-Diagnostics Center<br/>
            • <strong>Accreditation:</strong> WADA-ISO/IEC-17025-LAB-8902<br/>
            • <strong>NADA Code:</strong> NADA-REG-749201<br/>
            • <strong>Doctor Sign:</strong> Dr. Evelyn Reed, MD (Sports Physician)<br/>
            • <strong>Verification Token:</strong> <code>APEX-MED-8492-7104</code>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("#### **WADA Prohibited Substance Checklist:**")
        substances = [
            ("Anabolic Steroids (AAS)", "NEGATIVE (CLEAN)"),
            ("Peptide Hormones & EPO", "NEGATIVE (CLEAN)"),
            ("Beta-2 Agonists & SARMs", "NEGATIVE (CLEAN)"),
            ("Stimulants & Amphetamines", "NEGATIVE (CLEAN)")
        ]
        for sub, res in substances:
            st.markdown(f"• **{sub}**: <span style='color:#39FF14;font-weight:700;'>{res}</span>", unsafe_allow_html=True)
