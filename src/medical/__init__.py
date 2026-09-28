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

__all__ = [
    "MedicalSLAVerifier",
    "ComplianceStatus",
    "MedicalRecord",
    "ComplianceResult",
    "verify_medical_document",
]
