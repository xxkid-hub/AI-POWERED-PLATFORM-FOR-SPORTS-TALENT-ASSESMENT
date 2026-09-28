"""
ApexScout AI - 12-Component Biomechanical Telemetry Engine
Defines the telemetry schema, sport-specific presets, and automated score aggregators.
"""

from dataclasses import dataclass, asdict
from typing import Dict, Any


@dataclass
class BiomechanicsTelemetry:
    """Standardized 12-component biomechanical telemetry data model."""
    sport: str
    skill: str
    shot_result: str
    velocity_kmh: float
    drill_execution_quality: float  # Percentage 0-100%
    target_placement: str
    reaction_time_sec: float
    run_up_speed_kmh: float
    plant_foot_metric: str
    balance_rating: str
    follow_through: str
    contact_quality: str
    ball_curve_trajectory: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


_DEFAULT_SPORT_TELEMETRY = {
    "Soccer": BiomechanicsTelemetry(
        sport="Soccer",
        skill="Penalty Kick",
        shot_result="Goal (Top Corner)",
        velocity_kmh=91.4,
        drill_execution_quality=92.0,
        target_placement="Bottom Left Corner",
        reaction_time_sec=0.82,
        run_up_speed_kmh=18.4,
        plant_foot_metric="Good (35° ankle angle)",
        balance_rating="Excellent (Trunk upright)",
        follow_through="Good (Hips squared)",
        contact_quality="Clean (Instep sweet-spot)",
        ball_curve_trajectory="Slight Inside Curve",
    ),
    "Cricket": BiomechanicsTelemetry(
        sport="Cricket",
        skill="Outswinger Fast Bowling",
        shot_result="Hit Top of Off-Stump",
        velocity_kmh=138.6,
        drill_execution_quality=94.0,
        target_placement="Good Length (Outside Off)",
        reaction_time_sec=0.64,
        run_up_speed_kmh=24.8,
        plant_foot_metric="Front foot braced (178° lockout)",
        balance_rating="Optimal trunk stabilization",
        follow_through="Complete hip rotation",
        contact_quality="Clean 2.15m snap release",
        ball_curve_trajectory="Late 2.4° lateral outswing",
    ),
    "Kabaddi": BiomechanicsTelemetry(
        sport="Kabaddi",
        skill="Toe Touch & Dubki Raid",
        shot_result="2 Touch Points (Successful)",
        velocity_kmh=22.4,
        drill_execution_quality=96.0,
        target_placement="Bonus Line / Right Corner",
        reaction_time_sec=0.38,
        run_up_speed_kmh=16.2,
        plant_foot_metric="Low center of gravity (45° flex)",
        balance_rating="Superior ground recovery",
        follow_through="Rapid midline return",
        contact_quality="Precise 40ms touch tap",
        ball_curve_trajectory="Rapid zig-zag evasion arc",
    ),
    "Athletics": BiomechanicsTelemetry(
        sport="Athletics",
        skill="100m Sprint Start",
        shot_result="Sub-11s Pace Achieved",
        velocity_kmh=36.2,
        drill_execution_quality=93.5,
        target_placement="Midline Lane Preservation",
        reaction_time_sec=0.14,
        run_up_speed_kmh=36.2,
        plant_foot_metric="Explosive triple extension (175°)",
        balance_rating="Low drag aerodynamic posture",
        follow_through="Full stride cycle recovery",
        contact_quality="Forefoot striking (sub-110ms contact)",
        ball_curve_trajectory="Linear trajectory locked",
    ),
    "Basketball": BiomechanicsTelemetry(
        sport="Basketball",
        skill="Step-Back 3-Pointer",
        shot_result="Swish (Clean Release)",
        velocity_kmh=28.5,
        drill_execution_quality=91.0,
        target_placement="Center Cylinder",
        reaction_time_sec=0.55,
        run_up_speed_kmh=14.0,
        plant_foot_metric="Symmetrical load distribution",
        balance_rating="Vertical elevation alignment",
        follow_through="Gooseneck wrist snap locked",
        contact_quality="High fingertip roll",
        ball_curve_trajectory="Optimal 48° launch arc",
    ),
    "Volleyball": BiomechanicsTelemetry(
        sport="Volleyball",
        skill="Power Spike / Kill",
        shot_result="Point Scored (Cross-Court)",
        velocity_kmh=84.2,
        drill_execution_quality=89.5,
        target_placement="Deep Corner Line",
        reaction_time_sec=0.45,
        run_up_speed_kmh=17.5,
        plant_foot_metric="Dynamic penultimate stride brake",
        balance_rating="Core anti-rotation bracing",
        follow_through="Complete overhead whip follow",
        contact_quality="Full open palm contact",
        ball_curve_trajectory="Sharp downward steep angle",
    ),
}


def get_sport_telemetry_defaults(sport_name: str) -> BiomechanicsTelemetry:
    """Retrieves standard telemetry profile for a given sport."""
    canonical = sport_name.strip().title()
    return _DEFAULT_SPORT_TELEMETRY.get(
        canonical,
        _DEFAULT_SPORT_TELEMETRY["Soccer"]
    )


def compute_biomechanical_score(telemetry: BiomechanicsTelemetry) -> float:
    """
    Computes an aggregate biomechanical rating out of 100 based on velocity,
    execution quality, and reaction latency.
    """
    exec_score = telemetry.drill_execution_quality * 0.50
    # Reaction time penalty/bonus: sub-0.5s is excellent
    reaction_bonus = max(0.0, (1.0 - telemetry.reaction_time_sec)) * 25.0
    reaction_bonus = min(25.0, reaction_bonus)
    velocity_factor = min(25.0, (telemetry.velocity_kmh / 120.0) * 25.0)

    score = exec_score + reaction_bonus + velocity_factor
    return round(min(99.4, max(45.0, score)), 1)
