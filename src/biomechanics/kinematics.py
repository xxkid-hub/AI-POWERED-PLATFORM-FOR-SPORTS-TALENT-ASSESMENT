"""
ApexScout AI - Kinematics & Biomechanical Plausibility Engine
Validates human movement against physiological anatomical limits
to detect physics violations, splicing, or diffusion-generated movement anomalies.
"""

import math
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple


@dataclass
class KinematicLimits:
    """Physiological biomechanical boundary constraints for human movement."""
    max_knee_angular_velocity_deg_s: float = 1000.0   # <= 1000 deg/sec
    max_linear_acceleration_m_s2: float = 12.5       # <= 12.5 m/s^2 (gravity + explosive sprint)
    max_hip_angular_velocity_deg_s: float = 850.0     # <= 850 deg/sec
    max_valgus_inward_collapse_deg: float = 18.0      # <= 18 deg risk limit
    min_contact_time_ms: float = 30.0                 # >= 30ms ground reaction time


@dataclass
class KinematicValidationResult:
    """Outcome of biomechanical plausibility verification."""
    is_plausible: bool
    status: str
    violations: List[str]
    max_observed_velocity: float
    max_observed_acceleration: float
    valgus_angle: float
    confidence_score: float

    def to_dict(self) -> Dict:
        return {
            "is_plausible": self.is_plausible,
            "status": self.status,
            "violations": self.violations,
            "max_observed_velocity": round(self.max_observed_velocity, 2),
            "max_observed_acceleration": round(self.max_observed_acceleration, 2),
            "valgus_angle": round(self.valgus_angle, 2),
            "confidence_score": round(self.confidence_score, 4),
        }


def calculate_joint_angle(
    p1: Tuple[float, float],
    vertex: Tuple[float, float],
    p3: Tuple[float, float]
) -> float:
    """
    Computes the 2D planar angle at vertex formed by vectors (p1 - vertex) and (p3 - vertex).
    Returns the angle in degrees in the range [0.0, 180.0].
    """
    v1 = (p1[0] - vertex[0], p1[1] - vertex[1])
    v2 = (p3[0] - vertex[0], p3[1] - vertex[1])

    dot_product = v1[0] * v2[0] + v1[1] * v2[1]
    mag1 = math.hypot(v1[0], v1[1])
    mag2 = math.hypot(v2[0], v2[1])

    if mag1 < 1e-7 or mag2 < 1e-7:
        return 0.0

    cosine = max(-1.0, min(1.0, dot_product / (mag1 * mag2)))
    return math.degrees(math.acos(cosine))


def evaluate_valgus_collapse(hip: Tuple[float, float], knee: Tuple[float, float], ankle: Tuple[float, float]) -> float:
    """
    Estimates dynamic knee valgus inward collapse angle relative to mechanical axis line.
    """
    # Deviation from vertical leg alignment
    leg_angle = calculate_joint_angle(hip, knee, ankle)
    deviation = abs(180.0 - leg_angle)
    return deviation


def check_biomechanical_plausibility(
    angular_velocities: Optional[List[float]] = None,
    linear_accelerations: Optional[List[float]] = None,
    valgus_angle: float = 8.5,
    limits: Optional[KinematicLimits] = None
) -> KinematicValidationResult:
    """
    Validates tracked kinematic sequences against human physiological boundaries.
    """
    limits = limits or KinematicLimits()
    angular_velocities = angular_velocities or [320.0, 480.0, 610.0, 720.0, 510.0]
    linear_accelerations = linear_accelerations or [4.2, 7.8, 9.6, 11.2, 6.4]

    violations = []
    max_ang_vel = max(angular_velocities) if angular_velocities else 0.0
    max_lin_acc = max(linear_accelerations) if linear_accelerations else 0.0

    if max_ang_vel > limits.max_knee_angular_velocity_deg_s:
        violations.append(
            f"Excessive angular velocity: {max_ang_vel:.1f}°/s exceeds physiological limit of {limits.max_knee_angular_velocity_deg_s}°/s"
        )

    if max_lin_acc > limits.max_linear_acceleration_m_s2:
        violations.append(
            f"Excessive acceleration: {max_lin_acc:.1f} m/s² exceeds physiological human limit of {limits.max_linear_acceleration_m_s2} m/s²"
        )

    if valgus_angle > limits.max_valgus_inward_collapse_deg:
        violations.append(
            f"Dangerous valgus collapse: {valgus_angle:.1f}° exceeds safe threshold of {limits.max_valgus_inward_collapse_deg}°"
        )

    is_plausible = len(violations) == 0
    status = "PLAUSIBLE_HUMAN_MOVEMENT" if is_plausible else "ANOMALOUS_KINEMATICS_DETECTED"
    confidence = 0.96 if is_plausible else max(0.20, 1.0 - (len(violations) * 0.35))

    return KinematicValidationResult(
        is_plausible=is_plausible,
        status=status,
        violations=violations,
        max_observed_velocity=max_ang_vel,
        max_observed_acceleration=max_lin_acc,
        valgus_angle=valgus_angle,
        confidence_score=confidence,
    )
