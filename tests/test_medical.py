"""
Unit tests for the modular Medical & Anti-Doping SLA Compliance package.
"""

from datetime import datetime, timedelta, timezone
from src.medical import (
    MedicalSLAVerifier,
    ComplianceStatus,
    MedicalRecord,
    ComplianceResult,
    verify_medical_document,
)


def test_medical_sla_verified_within_24h():
    verifier = MedicalSLAVerifier()
    now = datetime.now(timezone.utc)
    rec = MedicalRecord(
        athlete_id="ATH-101",
        document_id="DOC-991",
        lab_name="WADA Lab Tokyo",
        test_type="Blood & Urine Screen",
        timestamp_utc=now - timedelta(hours=6),
        panel_result="NEGATIVE",
        accreditation_number="WADA-ACCREDITED-LAB-782",
    )
    result = verifier.evaluate_record(rec, current_time=now)
    assert result.status == ComplianceStatus.VERIFIED
    assert result.badge_color == "green"
    assert result.is_eligible_for_scouting is True


def test_medical_sla_provisional_grace_window():
    verifier = MedicalSLAVerifier()
    now = datetime.now(timezone.utc)
    rec = MedicalRecord(
        athlete_id="ATH-102",
        document_id="DOC-992",
        lab_name="WADA Lab London",
        test_type="Standard Sports Panel",
        timestamp_utc=now - timedelta(hours=34),
        panel_result="NEGATIVE",
        accreditation_number="WADA-ACCREDITED-LAB-782",
    )
    result = verifier.evaluate_record(rec, current_time=now)
    assert result.status == ComplianceStatus.PROVISIONAL
    assert result.badge_color == "yellow"
    assert result.is_eligible_for_scouting is True


def test_medical_sla_expired_delisted():
    verifier = MedicalSLAVerifier()
    now = datetime.now(timezone.utc)
    rec = MedicalRecord(
        athlete_id="ATH-103",
        document_id="DOC-993",
        lab_name="WADA Lab Cologne",
        test_type="Standard Sports Panel",
        timestamp_utc=now - timedelta(hours=55),
        panel_result="NEGATIVE",
        accreditation_number="WADA-ACCREDITED-LAB-782",
    )
    result = verifier.evaluate_record(rec, current_time=now)
    assert result.status == ComplianceStatus.DELISTED
    assert result.badge_color == "red"
    assert result.is_eligible_for_scouting is False


def test_medical_sla_positive_doping_delisted():
    verifier = MedicalSLAVerifier()
    now = datetime.now(timezone.utc)
    rec = MedicalRecord(
        athlete_id="ATH-104",
        document_id="DOC-994",
        lab_name="WADA Lab Sydney",
        test_type="Steroid Screen",
        timestamp_utc=now - timedelta(hours=2),
        panel_result="POSITIVE",
    )
    result = verifier.evaluate_record(rec, current_time=now)
    assert result.status == ComplianceStatus.DELISTED
    assert result.badge_color == "red"
    assert result.is_eligible_for_scouting is False


def test_verify_medical_document_helper():
    text = "WADA ACCREDITED LAB REPORT: ALL SUBSTANCES NEGATIVE. SIGNED DR. SMITH"
    res = verify_medical_document(text, athlete_id="ATH-200", timestamp_hours_ago=8.0)
    assert res.status == ComplianceStatus.VERIFIED
    assert isinstance(res.to_dict(), dict)


# =====================================================================
# Sports Injury Advisor & Emergency Tele-Triage Unit Tests
# =====================================================================

from src.medical import (
    detect_serious_injury,
    get_emergency_response,
    solve_basic_sports_injury,
    get_sports_physio_response,
    EMERGENCY_HOTLINE_NUMBER,
    AMBULANCE_NUMBER,
)


def test_detect_serious_injury_triggers():
    # Various serious trauma phrases
    assert detect_serious_injury("I think my teammate has a bone fracture") == "fracture"
    assert detect_serious_injury("His leg bone snapped in a tackle") in ["bone", "snap"]
    assert detect_serious_injury("Dislocation of the shoulder out of socket") == "dislocat"
    assert detect_serious_injury("He suffered a severe concussion and passed out") == "concussion"
    assert detect_serious_injury("Felt a loud pop and tore his ACL") == "pop"
    
    # Mild/basic injuries should not trigger serious red flag
    assert detect_serious_injury("im having sprained ankle from playing football") is None
    assert detect_serious_injury("jammed finger from catching volleyball") is None
    assert detect_serious_injury("mild hamstring tightness after cricket match") is None


def test_serious_injury_emergency_hotline_response():
    prompt = "Player leg snapped bone deformed cannot walk"
    response = get_sports_physio_response(prompt)
    assert "CRITICAL EMERGENCY MEDICAL ALERT" in response
    assert EMERGENCY_HOTLINE_NUMBER in response  # "1800-11-SPORTS"
    assert "Toll-Free" in response
    assert AMBULANCE_NUMBER in response  # "112 / 108"
    assert "DO NOT MOVE" in response


def test_football_basic_injury_solution():
    prompt = "im having sprained ankle from playing football"
    response = get_sports_physio_response(prompt)
    assert "Football Inversion Ankle Sprain" in response
    assert "P.R.I.C.E." in response
    assert "Ice" in response
    assert "Rehabilitation" in response
    assert EMERGENCY_HOTLINE_NUMBER in response  # Mentioned in escalation safety notice


def test_volleyball_basic_injury_solution():
    prompt = "having jumper knee patellar tendinopathy from volleyball jumping"
    response = get_sports_physio_response(prompt)
    assert "Volleyball Jumper's Knee" in response
    assert "tendon" in response.lower()
    assert "ice" in response.lower()


def test_basketball_basic_injury_solution():
    prompt = "jammed finger trying to catch basketball pass"
    response = get_sports_physio_response(prompt)
    assert "Basketball Jammed Finger" in response
    assert "buddy-tape" in response.lower() or "ice" in response.lower()


def test_kabaddi_basic_injury_solution():
    prompt = "defender caught my ankle in kabaddi ankle hold and twisted it"
    response = get_sports_physio_response(prompt)
    assert "Kabaddi Ankle Twist" in response
    assert "P.R.I.C.E." in response
    assert "rehabilitation" in response.lower()


def test_cricket_basic_injury_solution():
    prompt = "sharp side strain during fast bowling stride in cricket"
    response = get_sports_physio_response(prompt)
    assert "Cricket Fast Bowler's Side Strain" in response
    assert "oblique" in response.lower()
    assert "bowling" in response.lower()

