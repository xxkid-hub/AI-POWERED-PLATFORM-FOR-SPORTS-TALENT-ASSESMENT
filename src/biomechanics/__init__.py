"""
ApexScout AI - Biomechanics & Kinematics Package
Provides kinematic calculators, human movement plausibility filters,
and 12-component biomechanical telemetry structures.
"""

from .kinematics import (
    calculate_joint_angle,
    check_biomechanical_plausibility,
    evaluate_valgus_collapse,
    KinematicLimits,
    KinematicValidationResult,
)
from .telemetry import (
    BiomechanicsTelemetry,
    get_sport_telemetry_defaults,
    compute_biomechanical_score,
)

__all__ = [
    "calculate_joint_angle",
    "check_biomechanical_plausibility",
    "evaluate_valgus_collapse",
    "KinematicLimits",
    "KinematicValidationResult",
    "BiomechanicsTelemetry",
    "get_sport_telemetry_defaults",
    "compute_biomechanical_score",
]
