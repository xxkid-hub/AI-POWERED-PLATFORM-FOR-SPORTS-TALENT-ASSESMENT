"""
Unit tests for the modular Biomechanics & Kinematics package.
"""

import pytest
from src.biomechanics import (
    calculate_joint_angle,
    check_biomechanical_plausibility,
    evaluate_valgus_collapse,
    KinematicLimits,
    BiomechanicsTelemetry,
    get_sport_telemetry_defaults,
    compute_biomechanical_score,
)


def test_calculate_joint_angle_right_angle():
    # 90-degree right triangle at (0, 0)
    p1 = (0.0, 1.0)
    vertex = (0.0, 0.0)
    p3 = (1.0, 0.0)
    angle = calculate_joint_angle(p1, vertex, p3)
    assert pytest.approx(angle, 0.1) == 90.0


def test_calculate_joint_angle_straight_line():
    # 180-degree straight line
    p1 = (-1.0, 0.0)
    vertex = (0.0, 0.0)
    p3 = (1.0, 0.0)
    angle = calculate_joint_angle(p1, vertex, p3)
    assert pytest.approx(angle, 0.1) == 180.0


def test_evaluate_valgus_collapse():
    hip = (0.0, 2.0)
    knee = (0.0, 1.0)
    ankle = (0.0, 0.0)
    deviation = evaluate_valgus_collapse(hip, knee, ankle)
    assert deviation < 0.1


def test_check_biomechanical_plausibility_valid():
    res = check_biomechanical_plausibility(
        angular_velocities=[250.0, 400.0, 550.0],
        linear_accelerations=[3.0, 6.0, 8.5],
        valgus_angle=10.0,
    )
    assert res.is_plausible is True
    assert res.status == "PLAUSIBLE_HUMAN_MOVEMENT"
    assert len(res.violations) == 0


def test_check_biomechanical_plausibility_exceeded():
    res = check_biomechanical_plausibility(
        angular_velocities=[1250.0],  # > 1000 deg/s
        linear_accelerations=[22.0],  # > 12.5 m/s^2
        valgus_angle=25.0,            # > 18 deg
    )
    assert res.is_plausible is False
    assert res.status == "ANOMALOUS_KINEMATICS_DETECTED"
    assert len(res.violations) == 3


def test_sport_telemetry_defaults_and_scoring():
    for sport in ["Soccer", "Cricket", "Kabaddi", "Athletics", "Basketball", "Volleyball"]:
        telem = get_sport_telemetry_defaults(sport)
        assert isinstance(telem, BiomechanicsTelemetry)
        assert telem.sport == sport
        score = compute_biomechanical_score(telem)
        assert 50.0 <= score <= 100.0
