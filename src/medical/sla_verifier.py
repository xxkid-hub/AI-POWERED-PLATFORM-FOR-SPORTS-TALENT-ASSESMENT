"""
ApexScout AI - Medical SLA & Anti-Doping Verification Engine
Enforces 24-48 hour compliance windows, OCR accreditation parsing,
and 3-tier leaderboard eligibility badges.
"""

from dataclasses import dataclass, asdict
from datetime import datetime, timedelta, timezone
from enum import Enum
from typing import Dict, Any, Optional, List


class ComplianceStatus(str, Enum):
    VERIFIED = "VERIFIED"           # <= 24h: 🟢 Green Badge
    PROVISIONAL = "PROVISIONAL"     # 24h - 48h: 🟡 Yellow Badge
    DELISTED = "DELISTED"           # > 48h or Failed: 🔴 Red Badge


@dataclass
class MedicalRecord:
    """Medical & anti-doping submission record."""
    athlete_id: str
    document_id: str
    lab_name: str
    test_type: str
    timestamp_utc: datetime
    panel_result: str = "NEGATIVE"  # "NEGATIVE" or "POSITIVE"
    accreditation_number: Optional[str] = None


@dataclass
class ComplianceResult:
    """Verification decision with remaining SLA hours and badge color."""
    athlete_id: str
    status: ComplianceStatus
    badge_color: str
    badge_label: str
    hours_elapsed: float
    hours_remaining_sla: float
    is_eligible_for_scouting: bool
    verification_notes: List[str]

    def to_dict(self) -> Dict[str, Any]:
        data = asdict(self)
        data["status"] = self.status.value
        data["hours_elapsed"] = round(self.hours_elapsed, 1)
        data["hours_remaining_sla"] = round(self.hours_remaining_sla, 1)
        return data


class MedicalSLAVerifier:
    """Evaluates medical validity against 24h-48h WADA/NADA protocols."""

    def __init__(self, full_sla_hours: float = 24.0, grace_period_hours: float = 48.0):
        self.full_sla_hours = full_sla_hours
        self.grace_period_hours = grace_period_hours

    def evaluate_record(
        self,
        record: MedicalRecord,
        current_time: Optional[datetime] = None
    ) -> ComplianceResult:
        now = current_time or datetime.now(timezone.utc)
        record_dt = record.timestamp_utc
        if record_dt.tzinfo is None:
            record_dt = record_dt.replace(tzinfo=timezone.utc)

        delta = now - record_dt
        hours_elapsed = max(0.0, delta.total_seconds() / 3600.0)
        hours_remaining = max(0.0, self.grace_period_hours - hours_elapsed)

        notes = []

        if record.panel_result.upper() != "NEGATIVE":
            notes.append("Anti-doping panel non-compliant: Positive/Anomalous findings detected")
            return ComplianceResult(
                athlete_id=record.athlete_id,
                status=ComplianceStatus.DELISTED,
                badge_color="red",
                badge_label="🔴 Non-Compliant / Flagged",
                hours_elapsed=hours_elapsed,
                hours_remaining_sla=0.0,
                is_eligible_for_scouting=False,
                verification_notes=notes,
            )

        if record.accreditation_number and "WADA" not in record.accreditation_number.upper() and "NADA" not in record.accreditation_number.upper():
            notes.append("Unaccredited lab stamp: Requires WADA/NADA recognized certification")

        if hours_elapsed <= self.full_sla_hours:
            notes.append("Document verified within primary 24h SLA compliance window")
            return ComplianceResult(
                athlete_id=record.athlete_id,
                status=ComplianceStatus.VERIFIED,
                badge_color="green",
                badge_label="🟢 Verified Athlete (24h)",
                hours_elapsed=hours_elapsed,
                hours_remaining_sla=hours_remaining,
                is_eligible_for_scouting=True,
                verification_notes=notes,
            )
        elif hours_elapsed <= self.grace_period_hours:
            notes.append(f"Provisional grace period active: {hours_remaining:.1f}h remaining before delisting")
            return ComplianceResult(
                athlete_id=record.athlete_id,
                status=ComplianceStatus.PROVISIONAL,
                badge_color="yellow",
                badge_label="🟡 Provisional Grace (24-48h)",
                hours_elapsed=hours_elapsed,
                hours_remaining_sla=hours_remaining,
                is_eligible_for_scouting=True,
                verification_notes=notes,
            )
        else:
            notes.append(f"Verification window expired ({hours_elapsed:.1f}h > 48h limit): Delisted from public boards")
            return ComplianceResult(
                athlete_id=record.athlete_id,
                status=ComplianceStatus.DELISTED,
                badge_color="red",
                badge_label="🔴 Delisted (Expired > 48h)",
                hours_elapsed=hours_elapsed,
                hours_remaining_sla=0.0,
                is_eligible_for_scouting=False,
                verification_notes=notes,
            )


def verify_medical_document(
    document_text: str,
    athlete_id: str = "ATH-001",
    timestamp_hours_ago: float = 12.0
) -> ComplianceResult:
    """
    Simulates OCR document parsing and feeds into the SLA Verifier.
    """
    upper_doc = document_text.upper()
    is_positive = "POSITIVE" in upper_doc and "NEGATIVE" not in upper_doc
    panel = "POSITIVE" if is_positive else "NEGATIVE"

    accreditation = "WADA-ACCREDITED-LAB-782" if "WADA" in upper_doc or "NADA" in upper_doc else "GENERIC-CLINIC-99"

    record_dt = datetime.now(timezone.utc) - timedelta(hours=timestamp_hours_ago)
    rec = MedicalRecord(
        athlete_id=athlete_id,
        document_id=f"DOC-{abs(hash(document_text)) % 100000:05d}",
        lab_name="National Anti-Doping Testing Laboratory",
        test_type="Standard 10-Panel Sports Clearance",
        timestamp_utc=record_dt,
        panel_result=panel,
        accreditation_number=accreditation,
    )

    verifier = MedicalSLAVerifier()
    return verifier.evaluate_record(rec)
