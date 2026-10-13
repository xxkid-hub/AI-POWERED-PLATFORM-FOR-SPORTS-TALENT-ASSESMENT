"""
ApexScout AI - Coaches & Scouts Marketplace Tab
Renders certified scout profiles, interactive direct messaging dialogue,
and digital verified dossier dispatching.
"""

import random
import streamlit as st
from src.ui.mock_data import COACH_DIRECTORY
from src.ui.i18n import t, get_lang_code


@st.dialog("💬 Direct Message Coach")
def direct_message_dialog(coach: dict, language: str = "English"):
    coach_name = coach["name"]
    st.markdown(f"### {t('dlg_msg_to', language, name=coach_name)}")
    st.caption(t("dlg_msg_role_sport", language, role=coach['role'], sport=coach['sport'], loc=coach['loc']))
    st.markdown("---")

    lang_code = get_lang_code(language)
    sender_title = {
        "hi": "एलेक्स रिवेरा (आईडी: ATH-84920 - सत्यापित कंबाइन स्कोर: 94/100)",
        "es": "Alex Rivera (ID: ATH-84920 - Puntuación Verificada: 94/100)",
        "en": "Alex Rivera (ID: ATH-84920 - Verified Combine Score: 94/100)"
    }.get(lang_code, "Alex Rivera (ID: ATH-84920 - Verified Combine Score: 94/100)")

    st.text_input(t("dlg_msg_from", language), value=sender_title, disabled=True)

    templates = [
        t("tpl_custom", language),
        t("tpl_trial_req", language),
        t("tpl_roster_inq", language),
        t("tpl_feedback_req", language)
    ]

    template_choice = st.selectbox(
        t("dlg_msg_tpl_label", language),
        templates,
        key=f"tpl_{coach_name}"
    )

    default_body = ""
    if template_choice == t("tpl_trial_req", language):
        if lang_code == "hi":
            default_body = (
                f"आदरणीय कोच {coach_name},\n\n"
                f"मैंने हाल ही में {coach['sport']} के लिए अपना आधिकारिक एपेक्सस्काउट कंबाइन पूरा किया है, "
                f"जिसमें मेरा सत्यापित स्कोर 94/100 और उत्कृष्ट स्थिरता दर्ज की गई है। "
                f"मैं आगामी ट्रायल में भाग लेने के लिए आपके मार्गदर्शन का आकांक्षी हूँ।"
            )
        elif lang_code == "es":
            default_body = (
                f"Estimado/a Entrenador/a {coach_name},\n\n"
                f"Recientemente completé mi Combine oficial de ApexScout para {coach['sport']} con una puntuación "
                f"verificada de 94/100 y óptima estabilidad biomecánica. Me encantaría ser considerado/a para sus próximas pruebas."
            )
        else:
            default_body = (
                f"Dear Coach {coach_name},\n\n"
                f"I have recently completed my official ApexScout AI Combine for {coach['sport']} with a verified 94/100 "
                f"form score and optimal kinematic stability. I would be honored to be considered for your upcoming scouting trials."
            )
    elif template_choice == t("tpl_roster_inq", language):
        if lang_code == "hi":
            default_body = (
                f"आदरणीय कोच {coach_name},\n\n"
                f"मैं आगामी प्रतिभा ट्रायल, ग्रामीण विकास अनुदान और आपके कार्यक्रम के तहत उपलब्ध स्थानों के बारे में जानकारी प्राप्त करना चाहता हूँ।"
            )
        elif lang_code == "es":
            default_body = (
                f"Estimado/a Entrenador/a {coach_name},\n\n"
                f"Le escribo para consultar sobre próximas pruebas de talento, becas de desarrollo de base y plazas abiertas en su equipo."
            )
        else:
            default_body = (
                f"Dear Coach {coach_name},\n\n"
                f"I am writing to inquire about upcoming talent trials, grassroots sponsorship grants, and open roster slots "
                f"under your program for the upcoming season."
            )
    elif template_choice == t("tpl_feedback_req", language):
        if lang_code == "hi":
            default_body = (
                f"आदरणीय कोच {coach_name},\n\n"
                f"मैं अपनी हालिया कंबाइन रिपोर्ट, विशेष रूप से मेरे पैर के संतुलन और रिलीज तकनीक पर आपकी विशेषज्ञ प्रतिक्रिया का आकांक्षी हूँ।"
            )
        elif lang_code == "es":
            default_body = (
                f"Estimado/a Entrenador/a {coach_name},\n\n"
                f"Agradecería mucho sus comentarios expertos sobre mi informe cinemático reciente, en particular respecto a mi estabilidad de apoyo."
            )
        else:
            default_body = (
                f"Dear Coach {coach_name},\n\n"
                f"I would greatly appreciate your expert feedback on my recent combine kinetic report, particularly regarding my "
                f"plant-foot stability and release deceleration mechanics."
            )

    subj_default = {
        "hi": f"कंबाइन स्काउटिंग पूछताछ - {coach['sport']}",
        "es": f"Consulta de Ojeador Combine - {coach['sport']}",
        "en": f"Combine Scouting Inquiry - {coach['sport']}"
    }.get(lang_code, f"Combine Scouting Inquiry - {coach['sport']}")

    msg_subject = st.text_input(t("subject_label", language), value=subj_default, key=f"subj_{coach_name}")
    msg_body = st.text_area(
        t("body_label", language),
        value=default_body,
        height=140,
        placeholder="...",
        key=f"body_{coach_name}"
    )

    sent_key = f"sent_{coach_name}"
    trans_id_key = f"trans_id_{coach_name}"

    if sent_key in st.session_state and st.session_state[sent_key]:
        cur_id = st.session_state.get(trans_id_key, "MSG-84920")
        st.success(t("msg_sent_success_body", language, name=coach_name, trans_id=cur_id))
        if st.button(t("btn_close_dlg", language), key=f"close_{coach_name}", use_container_width=True):
            st.session_state[sent_key] = False
            st.rerun()
    else:
        col_send, col_cancel = st.columns([1.2, 1])
        with col_send:
            if st.button(t("btn_send", language), type="primary", key=f"btn_send_{coach_name}", use_container_width=True):
                if not msg_body.strip():
                    st.warning("Please type a message before clicking send.")
                else:
                    trans_id = f"MSG-{random.randint(10000, 99999)}"
                    st.session_state[sent_key] = True
                    st.session_state[trans_id_key] = trans_id
                    st.session_state["last_msg_coach"] = coach_name
                    st.toast(t("msg_sent_toast", language, name=coach_name), icon="📨")
                    st.rerun()

        with col_cancel:
            if st.button(t("btn_cancel", language), key=f"btn_cancel_{coach_name}", use_container_width=True):
                st.rerun()


@st.dialog("📋 Dispatch Official Verified Dossier")
def dispatch_dossier_dialog(coach: dict, language: str = "English"):
    coach_name = coach["name"]
    st.markdown(f"### {t('dlg_dossier_target', language, name=coach_name)}")
    st.caption(f"**Target:** {coach['role']} • **Combine Fee:** {coach['fee']}")
    st.markdown("---")

    st.markdown(t("dlg_dossier_info_box", language), unsafe_allow_html=True)

    dossier_key = f"dossier_sent_{coach_name}"
    if dossier_key in st.session_state and st.session_state[dossier_key]:
        st.success(t("dossier_sent_success_body", language, name=coach_name, role=coach['role']))
        if st.button(t("btn_close_dlg", language), key=f"close_dos_{coach_name}", use_container_width=True):
            st.session_state[dossier_key] = False
            st.rerun()
    else:
        info_txt = {
            "hi": f"डॉसियर भेजने पर **{coach_name}** को आपकी सत्यापित कंबाइन रिपोर्ट और वीडियो तक पूर्ण पहुंच प्राप्त होगी।",
            "es": f"El envío otorgará a **{coach_name}** acceso completo a tu informe de combine verificado y videos destacados.",
            "en": f"Dispatching will grant **{coach_name}** full access to your verified combine report and video highlights."
        }.get(get_lang_code(language), f"Dispatching will grant **{coach_name}** full access to your verified combine report and video highlights.")
        st.info(info_txt)

        col_confirm, col_cancel = st.columns([1.2, 1])
        with col_confirm:
            if st.button(t("btn_confirm_dossier", language), type="primary", key=f"btn_dos_confirm_{coach_name}", use_container_width=True):
                st.session_state[dossier_key] = True
                st.toast(t("dossier_sent_toast", language, name=coach_name), icon="📋")
                st.rerun()
        with col_cancel:
            if st.button(t("btn_cancel", language), key=f"btn_dos_cancel_{coach_name}", use_container_width=True):
                st.rerun()


def render_coaches_tab(language: str = "English"):
    st.title(t("coaches_title", language))
    st.markdown(t("coaches_subtitle", language))

    # Status banner if message was recently sent
    if st.session_state.get("last_msg_coach"):
        st.success(t("recent_msg_activity", language, name=st.session_state['last_msg_coach']))

    sport_lbl = t("sport_label", language)
    loc_lbl = t("location_label", language)
    fee_lbl = t("combine_fee_label", language)

    for c in COACH_DIRECTORY:
        with st.container():
            st.markdown(f"""
            <div class='card-box'>
                <h3>{c['name']} <span style='font-size:0.85rem;color:#00F2FE;'>• {c['role']}</span></h3>
                <p style='color:#94A3B8;'>{sport_lbl}: <strong>{c['sport']}</strong> | {loc_lbl}: <strong>{c['loc']}</strong> | {fee_lbl}: <span style='color:#39FF14;'>{c['fee']}</span></p>
            </div>
            """, unsafe_allow_html=True)

            col_b1, col_b2 = st.columns(2)
            with col_b1:
                btn_msg_text = t("btn_direct_message", language, name=c['name'])
                if st.button(btn_msg_text, key=f"msg_{c['name']}", use_container_width=True):
                    direct_message_dialog(c, language=language)

            with col_b2:
                btn_dos_text = t("btn_dispatch_dossier", language, name=c['name'])
                if st.button(btn_dos_text, key=f"dos_{c['name']}", use_container_width=True):
                    dispatch_dossier_dialog(c, language=language)


