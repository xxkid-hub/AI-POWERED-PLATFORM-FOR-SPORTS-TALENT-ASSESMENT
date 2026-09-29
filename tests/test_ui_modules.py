"""
Unit tests for the modular UI packages (mock data, audio synthesizer, design tokens).
"""

import wave
import io
from src.ui.mock_data import DRILLS_DATA, LEADERBOARD_RECORDS, COACH_DIRECTORY
from src.ui.audio import (
    generate_synthesized_chime_wav,
    generate_combine_start_chime,
    generate_liveness_verified_chime,
    get_audio_coach_script,
)
from src.ui.styles import SPORTS_TECH_CSS


def test_ui_drills_data_integrity():
    assert len(DRILLS_DATA) >= 4
    for name, drill in DRILLS_DATA.items():
        assert "skill" in drill
        assert "overall_rating" in drill
        assert 0 <= drill["overall_rating"] <= 100
        assert "accuracy" in drill


def test_ui_leaderboard_records():
    assert len(LEADERBOARD_RECORDS) >= 4
    for record in LEADERBOARD_RECORDS:
        assert "Rank" in record
        assert "Athlete" in record
        assert "Score" in record


def test_synthesized_audio_chime():
    raw_wav = generate_synthesized_chime_wav(frequency_hz=440.0, duration_seconds=0.2)
    assert len(raw_wav) > 100
    # Verify WAV header
    with wave.open(io.BytesIO(raw_wav), "rb") as wf:
        assert wf.getnchannels() == 1
        assert wf.getsampwidth() == 2
        assert wf.getframerate() == 16000
        assert wf.getnframes() > 0


def test_audio_coach_scripts_multilingual():
    for lang in ["English", "Hindi", "Español"]:
        script = get_audio_coach_script("Soccer", "Penalty", 95.0, language=lang)
        assert "title" in script
        assert "intro" in script
        assert "advice" in script


def test_sports_tech_css_tokens():
    assert "#080B11" in SPORTS_TECH_CSS
    assert "#00F2FE" in SPORTS_TECH_CSS
    assert "status-badge-green" in SPORTS_TECH_CSS
