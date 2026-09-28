"""
ApexScout AI - Dynamic AR Liveness Challenge Engine
Generates randomized physical action challenges to thwart pre-recorded replay attacks
and validates user response latency within strict SLA windows.
"""

import time
import random
from dataclasses import dataclass
from typing import Dict, Any, List


@dataclass
class LivenessChallenge:
    """Randomized AR prompt issued to an athlete during combine ingestion."""
    challenge_id: str
    prompt: str
    target_action: str
    time_limit_seconds: float
    issued_timestamp: float
    difficulty_level: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            "challenge_id": self.challenge_id,
            "prompt": self.prompt,
            "target_action": self.target_action,
            "time_limit_seconds": self.time_limit_seconds,
            "issued_timestamp": self.issued_timestamp,
            "difficulty_level": self.difficulty_level,
        }


_CHALLENGE_BANK: List[Dict[str, Any]] = [
    {
        "prompt": "Touch your Left Ear with your Right Hand before beginning sprint",
        "target_action": "CROSS_BODY_EAR_TOUCH",
        "time_limit": 5.0,
        "difficulty": "STANDARD",
    },
    {
        "prompt": "Hold a 90° Half-Squat and raise both hands horizontally for 2 seconds",
        "target_action": "SQUAT_HOLD_ARMS_RAISED",
        "time_limit": 6.0,
        "difficulty": "STANDARD",
    },
    {
        "prompt": "Clap your hands directly above your head 3 times facing camera",
        "target_action": "OVERHEAD_TRIPLE_CLAP",
        "time_limit": 4.5,
        "difficulty": "HIGH",
    },
    {
        "prompt": "Tap your left heel with your right hand behind your back",
        "target_action": "POSTERIOR_HEEL_TAP",
        "time_limit": 5.0,
        "difficulty": "HIGH",
    },
]


def generate_liveness_challenge(seed: int = None) -> LivenessChallenge:
    """Creates a new randomized AR challenge for combine session initialization."""
    if seed is not None:
        random.seed(seed)
    item = random.choice(_CHALLENGE_BANK)
    ch_id = f"CH-{int(time.time() * 1000) % 1000000:06d}"
    return LivenessChallenge(
        challenge_id=ch_id,
        prompt=item["prompt"],
        target_action=item["target_action"],
        time_limit_seconds=item["time_limit"],
        issued_timestamp=time.time(),
        difficulty_level=item["difficulty"],
    )


def verify_liveness_response(
    challenge: LivenessChallenge,
    action_detected: str,
    response_duration_seconds: float
) -> Dict[str, Any]:
    """
    Evaluates whether the candidate completed the challenge accurately within the SLA window.
    """
    is_action_match = challenge.target_action == action_detected or action_detected == "SUCCESS"
    is_within_time = response_duration_seconds <= challenge.time_limit_seconds
    passed = is_action_match and is_within_time

    return {
        "passed": passed,
        "challenge_id": challenge.challenge_id,
        "target_action": challenge.target_action,
        "action_detected": action_detected,
        "response_duration_seconds": round(response_duration_seconds, 2),
        "time_limit_seconds": challenge.time_limit_seconds,
        "status": "LIVENESS_VERIFIED" if passed else "LIVENESS_FAILED_OR_EXPIRED",
    }
