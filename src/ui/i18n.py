"""
ApexScout AI - Localization and Translation (i18n) Engine
Provides bilingual / trilingual localized UI strings for English, Hindi (हिन्दी), and Spanish (Español).
"""

from typing import Dict, Any


def get_lang_code(language_str: str) -> str:
    """Normalize language string to 'en', 'hi', or 'es'."""
    low = (language_str or "").lower()
    if "hindi" in low or "हिन्दी" in low or "hi" == low:
        return "hi"
    elif "español" in low or "spanish" in low or "es" == low:
        return "es"
    return "en"


TRANSLATIONS: Dict[str, Dict[str, str]] = {
    # -------------------------------------------------------------------------
    # SIDEBAR & COMMON
    # -------------------------------------------------------------------------
    "sidebar_title": {
        "en": "ApexScout AI",
        "hi": "एपेक्सस्काउट एआई",
        "es": "ApexScout IA"
    },
    "sidebar_tagline": {
        "en": "Vision-First Sports Scouting Ecosystem",
        "hi": "विजन-फर्स्ट खेल प्रतिभा खोज पारिस्थितिकी तंत्र",
        "es": "Ecosistema de Ojeadores Deportivos Basado en Visión"
    },
    "nav_combine": {
        "en": "Video & AR Combine Analysis",
        "hi": "वीडियो और एआर कंबाइन विश्लेषण",
        "es": "Análisis de Video y Combine AR"
    },
    "nav_ml_hub": {
        "en": "Custom ML Model & Dataset Hub",
        "hi": "कस्टम एमएल मॉडल और डेटासेट हब",
        "es": "Centro de Modelos ML y Datos"
    },
    "nav_medical": {
        "en": "24–48h Medical SLA & OCR",
        "hi": "24–48 घंटे मेडिकल एसएलए और ओसीआर",
        "es": "SLA Médico 24–48h y OCR"
    },
    "nav_progression": {
        "en": "Weekly AI Training & Peer Duels",
        "hi": "साप्ताहिक एआई प्रशिक्षण और सहकर्मी द्वंद्व",
        "es": "Entrenamiento Semanal IA y Duelos"
    },
    "nav_leaderboard": {
        "en": "Verified Scout Leaderboard",
        "hi": "सत्यापित स्काउट लीडरबोर्ड",
        "es": "Tabla de Líderes de Ojeadores Verificados"
    },
    "nav_coaches": {
        "en": "Coaches & Scouts Marketplace",
        "hi": "प्रमाणित कोच और स्काउट पोर्टल",
        "es": "Mercado de Entrenadores y Ojeadores"
    },
    "nav_helpline": {
        "en": "24/7 Helpline & Sports Physio",
        "hi": "24/7 हेल्पलाइन और स्पोर्ट्स फिजियो",
        "es": "Línea de Ayuda 24/7 y Fisioterapia"
    },
    "nav_passport": {
        "en": "Verifiable Digital Passport",
        "hi": "सत्यापनीय डिजिटल पासपोर्ट",
        "es": "Pasaporte Digital Verificable"
    },
    "rural_suite_title": {
        "en": "Rural & Grassroots Suite",
        "hi": "ग्रामीण और जमीनी स्तर सूट",
        "es": "Suite Rural y de Base"
    },
    "low_data_mode": {
        "en": "Low-Data Mode (<120 KB)",
        "hi": "लो-डेटा मोड (<120 KB)",
        "es": "Modo de Bajo Consumo (<120 KB)"
    },
    "low_data_active": {
        "en": "[ACTIVE] Video telemetry compressed for rural cellular networks.",
        "hi": "[सक्रिय] ग्रामीण सेलुलर नेटवर्क के लिए वीडियो टेलीमेट्री संपीड़ित है।",
        "es": "[ACTIVO] Telemetría de video comprimida para redes rurales."
    },
    "logged_in_as": {
        "en": "Logged in as: **Alex Rivera (Athlete)**",
        "hi": "लॉग इन किया गया: **एलेक्स रिवेरा (एथलीट)**",
        "es": "Sesión iniciada como: **Alex Rivera (Atleta)**"
    },

    # -------------------------------------------------------------------------
    # COACHES & SCOUTS MARKETPLACE TAB
    # -------------------------------------------------------------------------
    "coaches_title": {
        "en": "Certified Coaches & Grassroots Scout Portal",
        "hi": "प्रमाणित कोच और ग्रामीण प्रतिभा खोज पोर्टल",
        "es": "Portal de Entrenadores Certificados y Ojeadores de Base"
    },
    "coaches_subtitle": {
        "en": "Connect directly with verified collegiate scouts, UEFA/NBA development directors, and Olympic performance coaches.",
        "hi": "सत्यापित कॉलेज स्काउट्स, यूईएफए/एनबीए विकास निदेशकों और ओलंपिक प्रदर्शन कोचों से सीधे संपर्क करें।",
        "es": "Conéctate directamente con ojeadores universitarios verificados, directores de desarrollo UEFA/NBA y entrenadores olímpicos."
    },
    "sport_label": {
        "en": "Sport",
        "hi": "खेल",
        "es": "Deporte"
    },
    "location_label": {
        "en": "Location",
        "hi": "स्थान",
        "es": "Ubicación"
    },
    "combine_fee_label": {
        "en": "Combine Fee",
        "hi": "कंबाइन शुल्क",
        "es": "Tarifa de Evaluación"
    },
    "btn_direct_message": {
        "en": "💬 Direct Message {name}",
        "hi": "💬 {name} को सीधा संदेश भेजें",
        "es": "💬 Mensaje Directo a {name}"
    },
    "btn_dispatch_dossier": {
        "en": "📋 Dispatch Verified Dossier to {name}",
        "hi": "📋 {name} को सत्यापित डॉसियर भेजें",
        "es": "📋 Enviar Expediente Verificado a {name}"
    },
    "recent_msg_activity": {
        "en": "📬 **Recent Activity:** Your message was successfully sent to **{name}**!",
        "hi": "📬 **हाल की गतिविधि:** आपका संदेश सफलतापूर्वक **{name}** को भेज दिया गया है!",
        "es": "📬 **Actividad Reciente:** ¡Tu mensaje fue enviado con éxito a **{name}**!"
    },

    # -------------------------------------------------------------------------
    # MESSAGE DIALOG STRINGS
    # -------------------------------------------------------------------------
    "dlg_msg_title": {
        "en": "💬 Direct Message Coach",
        "hi": "💬 कोच को सीधा संदेश",
        "es": "💬 Mensaje Directo al Entrenador"
    },
    "dlg_msg_to": {
        "en": "Message to **{name}**",
        "hi": "**{name}** को संदेश भेजें",
        "es": "Mensaje para **{name}**"
    },
    "dlg_msg_role_sport": {
        "en": "**Role:** {role} • **Sport:** {sport} • **Location:** {loc}",
        "hi": "**भूमिका:** {role} • **खेल:** {sport} • **स्थान:** {loc}",
        "es": "**Rol:** {role} • **Deporte:** {sport} • **Ubicación:** {loc}"
    },
    "dlg_msg_from": {
        "en": "From (Athlete Profile):",
        "hi": "प्रेषक (एथलीट प्रोफ़ाइल):",
        "es": "De (Perfil del Atleta):"
    },
    "dlg_msg_tpl_label": {
        "en": "Choose a Message Template (Optional):",
        "hi": "एक संदेश टेम्पलेट चुनें (वैकल्पिक):",
        "es": "Elige una Plantilla de Mensaje (Opcional):"
    },
    "tpl_custom": {
        "en": "Custom Message",
        "hi": "कस्टम संदेश (स्वयं लिखें)",
        "es": "Mensaje Personalizado"
    },
    "tpl_trial_req": {
        "en": "Request Trial Evaluation & Combine Review",
        "hi": "ट्रायल मूल्यांकन और कंबाइन समीक्षा का अनुरोध",
        "es": "Solicitar Evaluación de Prueba y Revisión de Combine"
    },
    "tpl_roster_inq": {
        "en": "Inquiry Regarding Open Roster Spots & Academy Grants",
        "hi": "अकादमी रोस्टर और ग्रामीण अनुदान के संबंध में पूछताछ",
        "es": "Consulta sobre Plazas en el Equipo y Becas de Academia"
    },
    "tpl_feedback_req": {
        "en": "Request Biomechanical Form & Kinematic Feedback",
        "hi": "बायोमैकेनिकल फॉर्म और काइनेमैटिक प्रतिक्रिया का अनुरोध",
        "es": "Solicitar Comentarios Biomecánicos y Cinemáticos"
    },
    "subject_label": {
        "en": "Subject:",
        "hi": "विषय:",
        "es": "Asunto:"
    },
    "body_label": {
        "en": "Message Body:",
        "hi": "संदेश मुख्य भाग:",
        "es": "Cuerpo del Mensaje:"
    },
    "btn_send": {
        "en": "🚀 Send Message",
        "hi": "🚀 संदेश भेजें",
        "es": "🚀 Enviar Mensaje"
    },
    "btn_cancel": {
        "en": "Cancel",
        "hi": "रद्द करें",
        "es": "Cancelar"
    },
    "btn_close_dlg": {
        "en": "Close Dialogue",
        "hi": "संवाद बंद करें",
        "es": "Cerrar Diálogo"
    },
    "msg_sent_toast": {
        "en": "✅ Message sent successfully to {name}!",
        "hi": "✅ संदेश सफलतापूर्वक {name} को भेज दिया गया!",
        "es": "¡✅ Mensaje enviado exitosamente a {name}!"
    },
    "msg_sent_success_body": {
        "en": "🎉 **Message Sent!** Your message was successfully dispatched to **{name}**.\n\n- **Transmission ID:** `{trans_id}`\n- **Encrypted Channel:** 256-bit Scout Direct Connect\n- **Status:** Delivered to Scout Inbox",
        "hi": "🎉 **संदेश भेज दिया गया!** आपका संदेश सफलतापूर्वक **{name}** को प्रेषित किया गया।\n\n- **ट्रांसमिशन आईडी:** `{trans_id}`\n- **एन्क्रिप्टेड चैनल:** 256-बिट स्काउट डायरेक्ट कनेक्ट\n- **स्थिति:** स्काउट इनबॉक्स में वितरित",
        "es": "🎉 **¡Mensaje Enviado!** Tu mensaje fue enviado con éxito a **{name}**.\n\n- **ID de Transmisión:** `{trans_id}`\n- **Canal Encriptado:** Conexión Directa de Ojeador de 256 bits\n- **Estado:** Entregado en la Bandeja del Ojeador"
    },

    # -------------------------------------------------------------------------
    # DOSSIER DIALOG STRINGS
    # -------------------------------------------------------------------------
    "dlg_dossier_title": {
        "en": "📋 Dispatch Official Verified Dossier",
        "hi": "📋 आधिकारिक सत्यापित डॉसियर भेजें",
        "es": "📋 Enviar Expediente Oficial Verificado"
    },
    "dlg_dossier_target": {
        "en": "Dispatch Verified Dossier to **{name}**",
        "hi": "**{name}** को सत्यापित डॉसियर भेजें",
        "es": "Enviar Expediente Verificado a **{name}**"
    },
    "dlg_dossier_info_box": {
        "en": """
        <div style='background: rgba(0, 242, 254, 0.08); border: 1px solid rgba(0, 242, 254, 0.3); border-radius: 10px; padding: 1rem; margin-bottom: 1rem;'>
            <h4 style='color: #00F2FE; margin-top:0;'>📦 What is included in your Verified Dossier?</h4>
            <ul style='color: #CBD5E1; font-size: 0.9rem; margin-bottom: 0;'>
                <li><strong>✓ 12-Component Biomechanical Telemetry:</strong> Joint angles, knee valgus safety, limb velocities, and form score.</li>
                <li><strong>✓ 2D FFT & AR Anti-Spoofing Certificate:</strong> Cryptographic proof that video was recorded live without tampering or speedup.</li>
                <li><strong>✓ 24-48h WADA Anti-Doping Token:</strong> Verified negative lab panel or TUE exemption.</li>
                <li><strong>✓ Verifiable Digital Passport:</strong> Immutable SHA-256 biometric athlete hash (prevents age/identity fraud).</li>
            </ul>
        </div>
        """,
        "hi": """
        <div style='background: rgba(0, 242, 254, 0.08); border: 1px solid rgba(0, 242, 254, 0.3); border-radius: 10px; padding: 1rem; margin-bottom: 1rem;'>
            <h4 style='color: #00F2FE; margin-top:0;'>📦 आपके सत्यापित डॉसियर में क्या शामिल है?</h4>
            <ul style='color: #CBD5E1; font-size: 0.9rem; margin-bottom: 0;'>
                <li><strong>✓ 12-घटक बायोमैकेनिकल टेलीमेट्री:</strong> जोड़ कोण, घुटने का वालगस सुरक्षा कोण, अंग वेग और फॉर्म स्कोर।</li>
                <li><strong>✓ 2D FFT और AR एंटी-स्पूफिंग प्रमाणपत्र:</strong> वीडियो लाइव रिकॉर्ड किया गया है और इसमें कोई छेड़छाड़ या गति नहीं है।</li>
                <li><strong>✓ 24-48 घंटे वाडा (WADA) एंटी-डोपिंग टोकन:</strong> सत्यापित नकारात्मक प्रयोगशाला परिणाम।</li>
                <li><strong>✓ सत्यापनीय डिजिटल पासपोर्ट:</strong> अपरिवर्तनीय SHA-256 बायोमेट्रिक एथलीट हैश (पहचान और उम्र धोखाधड़ी रोकता है)।</li>
            </ul>
        </div>
        """,
        "es": """
        <div style='background: rgba(0, 242, 254, 0.08); border: 1px solid rgba(0, 242, 254, 0.3); border-radius: 10px; padding: 1rem; margin-bottom: 1rem;'>
            <h4 style='color: #00F2FE; margin-top:0;'>📦 ¿Qué incluye tu Expediente Verificado?</h4>
            <ul style='color: #CBD5E1; font-size: 0.9rem; margin-bottom: 0;'>
                <li><strong>✓ Telemetría Biomecánica de 12 Componentes:</strong> Ángulos articulares, seguridad de valgo de rodilla, velocidades de extremidades y puntuación técnica.</li>
                <li><strong>✓ Certificado Antimanipulación 2D FFT y AR:</strong> Prueba criptográfica de que el video fue grabado en vivo sin aceleración ni trucos.</li>
                <li><strong>✓ Token Antidopaje WADA de 24-48h:</strong> Panel de laboratorio negativo verificado o exención TUE.</li>
                <li><strong>✓ Pasaporte Digital Verificable:</strong> Hash biométrico inmutable SHA-256 (previene fraude de identidad o edad).</li>
            </ul>
        </div>
        """
    },
    "btn_confirm_dossier": {
        "en": "📤 Confirm & Dispatch Dossier",
        "hi": "📤 पुष्टि करें और डॉसियर भेजें",
        "es": "📤 Confirmar y Enviar Expediente"
    },
    "dossier_sent_toast": {
        "en": "✅ Verified Dossier dispatched to {name}!",
        "hi": "✅ सत्यापित डॉसियर सफलतापूर्वक {name} को भेज दिया गया!",
        "es": "¡✅ Expediente Verificado enviado a {name}!"
    },
    "dossier_sent_success_body": {
        "en": "✓ **Official Dossier Dispatched!** Delivered to **{name}'s** verified scout portal.\n\n- **Dossier Serial:** `DOS-77491-VERIFIED`\n- **Recipient:** {name} ({role})\n- **Status:** Awaiting Scout Review",
        "hi": "✓ **आधिकारिक डॉसियर प्रेषित!** **{name}** के सत्यापित स्काउट पोर्टल पर वितरित।\n\n- **डॉसियर सीरियल:** `DOS-77491-VERIFIED`\n- **प्राप्तकर्ता:** {name} ({role})\n- **स्थिति:** स्काउट समीक्षा की प्रतीक्षा में",
        "es": "✓ **¡Expediente Oficial Enviado!** Entregado en el portal verificado de **{name}**.\n\n- **Serie del Expediente:** `DOS-77491-VERIFIED`\n- **Destinatario:** {name} ({role})\n- **Estado:** En espera de revisión del ojeador"
    }
}


def t(key: str, language: str = "English", **kwargs: Any) -> str:
    """
    Look up a localized string by key and language.
    Falls back to English if key or language is not found.
    Interpolates any provided kwargs.
    """
    code = get_lang_code(language)
    entry = TRANSLATIONS.get(key)
    if not entry:
        return key

    text = entry.get(code) or entry.get("en") or key
    if kwargs:
        try:
            return text.format(**kwargs)
        except Exception:
            return text
    return text
