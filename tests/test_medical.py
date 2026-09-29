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
