"""
ApexScout AI - Medical & Anti-Doping Compliance Package
Implements the strict 24-48h SLA verification engine, WADA/NADA OCR document analysis,
and 3-tier athlete badge status management.
"""

from .sla_verifier import (
    MedicalSLAVerifier,
    ComplianceStatus,
    MedicalRecord,
    ComplianceResult,
    verify_medical_document,
)
from .sports_injury_advisor import (
    get_sports_physio_response,
    detect_serious_injury,
    solve_basic_sports_injury,
    get_emergency_response,
    EMERGENCY_HOTLINE_NUMBER,
    AMBULANCE_NUMBER,
)

__all__ = [
    "MedicalSLAVerifier",
    "ComplianceStatus",
    "MedicalRecord",
    "ComplianceResult",
    "verify_medical_document",
    "get_sports_physio_response",
    "detect_serious_injury",
    "solve_basic_sports_injury",
    "get_emergency_response",
    "EMERGENCY_HOTLINE_NUMBER",
    "AMBULANCE_NUMBER",
]
