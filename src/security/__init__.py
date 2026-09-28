"""
ApexScout AI - Security & Integrity Guard Package
Provides spatial-frequency 2D FFT deepfake/diffusion artifact detection
and dynamic AR liveness challenge verification.
"""

from .fft_detector import (
    analyze_spatial_frequency_fft,
    FFTAnalysisResult,
)
from .liveness import (
    generate_liveness_challenge,
    verify_liveness_response,
    LivenessChallenge,
)

__all__ = [
    "analyze_spatial_frequency_fft",
    "FFTAnalysisResult",
    "generate_liveness_challenge",
    "verify_liveness_response",
    "LivenessChallenge",
]
