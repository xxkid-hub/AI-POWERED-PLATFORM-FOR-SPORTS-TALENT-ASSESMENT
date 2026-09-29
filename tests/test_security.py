"""
Unit tests for the modular Security & Anti-Deepfake package.
"""

import numpy as np
from PIL import Image
from src.security import (
    analyze_spatial_frequency_fft,
    FFTAnalysisResult,
    generate_liveness_challenge,
    verify_liveness_response,
    LivenessChallenge,
)


def test_fft_analysis_synthetic_array():
    arr = np.random.uniform(50, 200, (128, 128)).astype(np.uint8)
    res = analyze_spatial_frequency_fft(arr)
    assert isinstance(res, FFTAnalysisResult)
    assert res.high_freq_ratio >= 0.0
    assert 0.0 <= res.tamper_probability <= 1.0
    assert 0.0 <= res.integrity_score <= 100.0


def test_fft_analysis_pil_image():
    # Textured image with gradients
    arr = np.linspace(0, 255, 64 * 64, dtype=np.uint8).reshape((64, 64))
    img = Image.fromarray(arr)
    res = analyze_spatial_frequency_fft(img)
    assert isinstance(res, FFTAnalysisResult)
    assert isinstance(res.to_dict(), dict)

    # Completely flat solid color correctly triggers anomaly flag
    flat_img = Image.new("RGB", (64, 64), color=(128, 128, 128))
    flat_res = analyze_spatial_frequency_fft(flat_img)
    assert flat_res.is_authentic is False


def test_liveness_challenge_generation():
    challenge = generate_liveness_challenge(seed=42)
    assert isinstance(challenge, LivenessChallenge)
    assert challenge.challenge_id.startswith("CH-")
    assert len(challenge.prompt) > 5
    assert challenge.time_limit_seconds > 0.0


def test_liveness_verification_success():
    challenge = generate_liveness_challenge(seed=10)
    result = verify_liveness_response(
        challenge=challenge,
        action_detected=challenge.target_action,
        response_duration_seconds=2.5,
    )
    assert result["passed"] is True
    assert result["status"] == "LIVENESS_VERIFIED"


def test_liveness_verification_failure_mismatch():
    challenge = generate_liveness_challenge(seed=10)
    result = verify_liveness_response(
        challenge=challenge,
        action_detected="WRONG_ACTION",
        response_duration_seconds=2.5,
    )
    assert result["passed"] is False
    assert result["status"] == "LIVENESS_FAILED_OR_EXPIRED"


def test_liveness_verification_failure_timeout():
    challenge = generate_liveness_challenge(seed=10)
    result = verify_liveness_response(
        challenge=challenge,
        action_detected=challenge.target_action,
        response_duration_seconds=challenge.time_limit_seconds + 3.0,
    )
    assert result["passed"] is False
    assert result["status"] == "LIVENESS_FAILED_OR_EXPIRED"
