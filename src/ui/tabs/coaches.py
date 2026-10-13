"""
ApexScout AI - Coaches & Scouts Marketplace Tab
Renders certified scout profiles, interactive direct messaging dialogue,
and digital verified dossier dispatching.
"""

import random
import streamlit as st
from src.ui.mock_data import COACH_DIRECTORY


@st.dialog("💬 Direct Message Coach")
def direct_message_dialog(coach: dict):
    st.markdown(f"### Message to **{coach['name']}**")
    st.caption(f"**Role:** {coach['role']} • **Sport:** {coach['sport']} • **Location:** {coach['loc']}")
    st.markdown("---")

    sender = st.text_input("From (Athlete Profile):", value="Alex Rivera (ID: ATH-84920 - Verified Combine Score: 94/100)", disabled=True)

    template_choice = st.selectbox(
        "Choose a Message Template (Optional):",
        [
            "Custom Message",
            "Request Trial Evaluation & Combine Review",
            "Inquiry Regarding Open Roster Spots & Academy Grants",
            "Request Biomechanical Form & Kinematic Feedback"
        ],
        key=f"tpl_{coach['name']}"
    )

    default_body = ""
    if template_choice == "Request Trial Evaluation & Combine Review":
        default_body = (
            f"Dear Coach {coach['name']},\n\n"
            f"I have recently completed my official ApexScout AI Combine for {coach['sport']} with a verified 94/100 "
            f"form score and optimal kinematic stability. I would be honored to be considered for your upcoming scouting trials."
        )
    elif template_choice == "Inquiry Regarding Open Roster Spots & Academy Grants":
        default_body = (
            f"Dear Coach {coach['name']},\n\n"
            f"I am writing to inquire about upcoming talent trials, grassroots sponsorship grants, and open roster slots "
            f"under your program for the upcoming season."
        )
    elif template_choice == "Request Biomechanical Form & Kinematic Feedback":
        default_body = (
            f"Dear Coach {coach['name']},\n\n"
            f"I would greatly appreciate your expert feedback on my recent combine kinetic report, particularly regarding my "
            f"plant-foot stability and release deceleration mechanics."
        )

    msg_subject = st.text_input("Subject:", value=f"Combine Scouting Inquiry - {coach['sport']}", key=f"subj_{coach['name']}")
    msg_body = st.text_area(
        "Message Body:",
        value=default_body,
        height=140,
        placeholder="Type your message to the coach here...",
        key=f"body_{coach['name']}"
    )

    if f"sent_{coach['name']}" in st.session_state and st.session_state[f"sent_{coach['name']}"]:
        st.success(f"🎉 **Message Sent!** Your message was successfully dispatched to **{coach['name']}**.\n\n"
                   f"- **Transmission ID:** `{st.session_state.get(f'trans_id_{coach[\"name\"]}', 'MSG-84920')}`\n"
                   f"- **Encrypted Channel:** 256-bit Scout Direct Connect\n"
                   f"- **Status:** Delivered to Scout Inbox")
        if st.button("Close Dialogue", key=f"close_{coach['name']}", use_container_width=True):
            st.session_state[f"sent_{coach['name']}"] = False
            st.rerun()
    else:
        col_send, col_cancel = st.columns([1.2, 1])
        with col_send:
            if st.button("🚀 Send Message", type="primary", key=f"btn_send_{coach['name']}", use_container_width=True):
                if not msg_body.strip():
                    st.warning("Please type a message before clicking send.")
                else:
                    trans_id = f"MSG-{random.randint(10000, 99999)}"
                    st.session_state[f"sent_{coach['name']}"] = True
                    st.session_state[f"trans_id_{coach['name']}"] = trans_id
                    st.session_state[f"last_msg_coach"] = coach['name']
                    st.toast(f"✅ Message sent successfully to {coach['name']}!", icon="📨")
                    st.rerun()

        with col_cancel:
            if st.button("Cancel", key=f"btn_cancel_{coach['name']}", use_container_width=True):
                st.rerun()


@st.dialog("📋 Dispatch Official Verified Dossier")
def dispatch_dossier_dialog(coach: dict):
    st.markdown(f"### Dispatch Verified Dossier to **{coach['name']}**")
    st.caption(f"**Target:** {coach['role']} • **Combine Fee:** {coach['fee']}")
    st.markdown("---")

    st.markdown("""
    <div style='background: rgba(0, 242, 254, 0.08); border: 1px solid rgba(0, 242, 254, 0.3); border-radius: 10px; padding: 1rem; margin-bottom: 1rem;'>
        <h4 style='color: #00F2FE; margin-top:0;'>📦 What is included in your Verified Dossier?</h4>
        <ul style='color: #CBD5E1; font-size: 0.9rem; margin-bottom: 0;'>
            <li><strong>✓ 12-Component Biomechanical Telemetry:</strong> Joint angles, knee valgus safety, limb velocities, and form score.</li>
            <li><strong>✓ 2D FFT & AR Anti-Spoofing Certificate:</strong> Cryptographic proof that video was recorded live without tampering or speedup.</li>
            <li><strong>✓ 24-48h WADA Anti-Doping Token:</strong> Verified negative lab panel or TUE exemption.</li>
            <li><strong>✓ Verifiable Digital Passport:</strong> Immutable SHA-256 biometric athlete hash (prevents age/identity fraud).</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    if f"dossier_sent_{coach['name']}" in st.session_state and st.session_state[f"dossier_sent_{coach['name']}"]:
        st.success(f"✓ **Official Dossier Dispatched!** Delivered to **{coach['name']}'s** verified scout portal.\n\n"
                   f"- **Dossier Serial:** `DOS-77491-VERIFIED`\n"
                   f"- **Recipient:** {coach['name']} ({coach['role']})\n"
                   f"- **Status:** Awaiting Scout Review")
        if st.button("Close Dialogue", key=f"close_dos_{coach['name']}", use_container_width=True):
            st.session_state[f"dossier_sent_{coach['name']}"] = False
            st.rerun()
    else:
        st.info(f"Dispatching will grant **{coach['name']}** full access to your verified combine report and video highlights.")
        col_confirm, col_cancel = st.columns([1.2, 1])
        with col_confirm:
            if st.button("📤 Confirm & Dispatch Dossier", type="primary", key=f"btn_dos_confirm_{coach['name']}", use_container_width=True):
                st.session_state[f"dossier_sent_{coach['name']}"] = True
                st.toast(f"✅ Verified Dossier dispatched to {coach['name']}!", icon="📋")
                st.rerun()
        with col_cancel:
            if st.button("Cancel", key=f"btn_dos_cancel_{coach['name']}", use_container_width=True):
                st.rerun()


def render_coaches_tab():
    st.title("Certified Coaches & Grassroots Scout Portal")
    st.markdown("Connect directly with verified collegiate scouts, UEFA/NBA development directors, and Olympic performance coaches.")

    # Status banner if message was recently sent
    if st.session_state.get("last_msg_coach"):
        st.success(f"📬 **Recent Activity:** Your message was successfully sent to **{st.session_state['last_msg_coach']}**!")

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
                if st.button(f"💬 Direct Message {c['name']}", key=f"msg_{c['name']}", use_container_width=True):
                    direct_message_dialog(c)

            with col_b2:
                if st.button(f"📋 Dispatch Verified Dossier to {c['name']}", key=f"dos_{c['name']}", use_container_width=True):
                    dispatch_dossier_dialog(c)

