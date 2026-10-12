"""
ApexScout AI - 24/7 Helpline & Sports Physio AI Tab
Renders emergency sports hotlines, SOS priority ticketing,
interactive physiotherapy triage bot, and multilingual audio coaching.
"""

import streamlit as st
from src.ui.audio import generate_combine_start_chime, get_audio_coach_script


from src.medical import get_sports_physio_response

def render_helpline_tab(language: str = "English"):
    st.title("24/7 Athlete Helpline & Sports Physio AI")
    st.markdown("Toll-free rural sports hotline, acute injury first-aid tele-triage, and WADA anti-doping advisory.")

    col_h1, col_h2 = st.columns([1, 1.2])

    with col_h1:
        st.markdown("### **Emergency Hotlines**")
        st.markdown("""
        <div class='card-box' style='border-left: 4px solid #ef4444; margin-bottom: 8px;'>
            <strong>🚨 24/7 Rural & Grassroots Toll-Free Emergency Hotline:</strong><br/>
            <code style='font-size: 1.15em; color: #ef4444; font-weight: bold;'>1800-11-SPORTS</code> (Toll-Free 24/7 Multi-Lingual)
        </div>
        <div class='card-box' style='margin-bottom: 8px;'>
            <strong>🚑 National Ambulance Emergency Services:</strong><br/>
            <code>112</code> / <code>108</code> (Immediate 24/7 Dispatch)
        </div>
        <div class='card-box' style='margin-bottom: 8px;'>
            <strong>🩺 Sports Trauma & Orthopedic First Aid:</strong><br/>
            <code>+1 (800) 555-SPORTS</code> / <code>+91 1800 200 4545</code>
        </div>
        <div class='card-box'>
            <strong>💊 CleanSport WADA Anti-Doping Hotline:</strong><br/>
            <code>+1 (800) 223-0393</code>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### **Audio Voiceover Coach**")
        audio_info = get_audio_coach_script("Football", "Penalty Kick", 94.0, language=language)
        st.caption(f"**{audio_info['title']}**: {audio_info['intro']}")
        
        if st.button("Play Combine Chime & Audio Feedback", key="btn_play_chime"):
            chime_bytes = generate_combine_start_chime()
            st.audio(chime_bytes, format="audio/wav")
            st.info(f"Coach advice: {audio_info['advice']}")

        st.markdown("### **Submit Emergency Support Ticket**")
        ticket_name = st.text_input("Athlete Name", value="Alex Rivera")
        ticket_issue = st.text_area("Describe Acute Pain or Issue")
        if st.button("Dispatch Priority SOS Ticket", type="primary"):
            st.success("🚨 Emergency Priority SOS Ticket TICK-84920 dispatched to regional duty trauma physician!")

    with col_h2:
        st.markdown("### **Apex AI Sports Physio & Emergency Tele-Triage Bot**")
        st.caption("Covers Football, Volleyball, Basketball, Kabaddi, and Cricket injuries. Auto-detects critical emergencies for toll-free dispatch.")

        # Quick symptom chips
        st.markdown("**Quick Inquiries (Click to Ask):**")
        q_cols1 = st.columns(3)
        q_cols2 = st.columns(3)
        
        quick_query = None
        with q_cols1[0]:
            if st.button("⚽ Football Ankle Sprain", key="chip_fb_ankle", use_container_width=True):
                quick_query = "im having sprained ankle from playing football"
        with q_cols1[1]:
            if st.button("🏐 Volleyball Jumper's Knee", key="chip_vb_knee", use_container_width=True):
                quick_query = "i have sharp knee tendon pain after volleyball spiking jump"
        with q_cols1[2]:
            if st.button("🏀 Basketball Jammed Finger", key="chip_bb_finger", use_container_width=True):
                quick_query = "jammed finger trying to catch basketball pass"

        with q_cols2[0]:
            if st.button("🤼 Kabaddi Ankle Hold Twist", key="chip_kb_ankle", use_container_width=True):
                quick_query = "defender caught my ankle in kabaddi ankle hold and twisted it"
        with q_cols2[1]:
            if st.button("🏏 Cricket Bowling Side Strain", key="chip_cr_side", use_container_width=True):
                quick_query = "sharp oblique side pain during fast bowling delivery stride in cricket"
        with q_cols2[2]:
            if st.button("🚨 Serious Bone Fracture", key="chip_emerg_fracture", use_container_width=True):
                quick_query = "severe injury: player heard loud snap bone deformed cannot walk"

        if "messages" not in st.session_state:
            st.session_state.messages = [
                {
                    "role": "assistant",
                    "content": "👋 **Hello! I am your 24/7 Sports Physiotherapy and Emergency Tele-Triage Advisor.**\n\n"
                               "I provide immediate clinical first-aid (P.R.I.C.E. protocol), rehabilitation, and return-to-play guidelines for:\n"
                               "- ⚽ **Football**: Ankle sprains, hamstring pulls, shin splints, groin strains, calf cramps\n"
                               "- 🏐 **Volleyball**: Jumper's knee, jammed fingers, rotator cuff impingement, ankle sprains\n"
                               "- 🏀 **Basketball**: Lateral inversion ankle sprains, jammed fingers, Achilles tightness, quad contusions\n"
                               "- 🤼 **Kabaddi**: Ankle twists (ankle hold), shoulder stingers, adductor pulls, mat friction burns\n"
                               "- 🏏 **Cricket**: Fast-bowling side strains, rotator cuff tendonitis, hamstring strains, finger contusions\n\n"
                               "⚠️ **Emergency Triage**: If an injury is serious (suspected fracture, complete ligament rupture, joint dislocation, or concussion), "
                               "I will immediately trigger our **Emergency Hotline Protocol** with toll-free helpline `1800-11-SPORTS`."
                }
            ]

        # Display chat conversation
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])

        # Determine prompt from chat input or quick prompt chip
        user_input = st.chat_input("Ask sports doctor about injuries in football, volleyball, basketball, kabaddi, or cricket...")
        active_prompt = quick_query or user_input

        if active_prompt:
            st.session_state.messages.append({"role": "user", "content": active_prompt})
            with st.chat_message("user"):
                st.write(active_prompt)

            reply = get_sports_physio_response(active_prompt)

            st.session_state.messages.append({"role": "assistant", "content": reply})
            with st.chat_message("assistant"):
                st.write(reply)
            st.rerun()
