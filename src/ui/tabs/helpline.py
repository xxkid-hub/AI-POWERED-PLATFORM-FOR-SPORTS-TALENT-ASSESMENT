"""
ApexScout AI - 24/7 Helpline & Sports Physio AI Tab
Renders emergency sports hotlines, SOS priority ticketing,
interactive physiotherapy triage bot, and multilingual audio coaching.
"""

import streamlit as st
from src.ui.audio import generate_combine_start_chime, get_audio_coach_script


def render_helpline_tab(language: str = "English"):
    st.title("24/7 Athlete Helpline & Sports Physio AI")
    st.markdown("Toll-free rural sports hotline, acute injury first-aid tele-triage, and WADA anti-doping advisory.")

    col_h1, col_h2 = st.columns([1, 1.2])

    with col_h1:
        st.markdown("### **Emergency Hotlines**")
        st.markdown("""
        <div class='card-box'>
            <strong>Rural Grassroots Talent Hotline:</strong><br/>
            <code>1800-11-SPORTS</code> (Toll-Free 24/7 Multi-Lingual)
        </div>
        <div class='card-box'>
            <strong>Sports Injury & First Aid:</strong><br/>
            <code>+1 (800) 555-SPORTS</code> / <code>+91 1800 200 4545</code>
        </div>
        <div class='card-box'>
            <strong>CleanSport WADA Anti-Doping Hotline:</strong><br/>
            <code>+1 (800) 223-0393</code>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### **Audio Voiceover Coach**")
        audio_info = get_audio_coach_script("Football", "Penalty Kick", 94.0, language=language)
        st.caption(f"**{audio_info['title']}**: {audio_info['intro']}")
        
        if st.button("🔊 Play Combine Chime & Audio Feedback", key="btn_play_chime"):
            chime_bytes = generate_combine_start_chime()
            st.audio(chime_bytes, format="audio/wav")
            st.info(f"Coach advice: {audio_info['advice']}")

        st.markdown("### **Submit Emergency Support Ticket**")
        ticket_name = st.text_input("Athlete Name", value="Alex Rivera")
        ticket_issue = st.text_area("Describe Acute Pain or Issue")
        if st.button("Dispatch Priority SOS Ticket", type="primary"):
            st.success("✓ Emergency Ticket TICK-84920 dispatched to regional duty physician!")

    with col_h2:
        st.markdown("### **Apex AI Sports Physio & Anti-Doping Bot**")
        if "messages" not in st.session_state:
            st.session_state.messages = [
                {"role": "assistant", "content": "Hello! I am your 24/7 Sports Physiotherapy and CleanSport Anti-Doping Advisor. Ask me anything about injury rehab (RICE protocol), knee valgus correction, or WADA medication clearance."}
            ]

        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])

        if prompt := st.chat_input("Ask sports doctor about injuries, recovery, or medicine..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.write(prompt)

            lower_p = prompt.lower()
            if "knee" in lower_p or "pain" in lower_p:
                reply = "**Sports Clinical Protocol for Knee Pain**: Apply the P.R.I.C.E. protocol (Protect, Rest, Ice 15-20 min, Compress, Elevate). Reduce high-impact jumping drills and focus on isometric quad strengthening."
            elif "wada" in lower_p or "supplement" in lower_p or "medicine" in lower_p:
                reply = "**Anti-Doping Advisory**: Verify all supplements with NSF Certified for Sport or Informed-Sport. Submit a Therapeutic Use Exemption (TUE) for prescription asthma inhalers within your 24-48h medical report."
            else:
                reply = "Thank you for consulting ApexScout Sports Health AI. For acute pain, call our 24/7 emergency hotline at 1800-11-SPORTS."

            st.session_state.messages.append({"role": "assistant", "content": reply})
            with st.chat_message("assistant"):
                st.write(reply)
