"""
Unit Tests for SportsImagePreprocessor & Feature Extraction
Covers BGR frames, PIL images, dimension consistency, and invalid inputs.
"""

import os
import pytest
import numpy as np
from PIL import Image

from src.preprocessor import (
    SportsImagePreprocessor,
    ImagePreprocessor,
    extract_features_from_image,
    preprocess_frame,
    preprocess_pil
)

@pytest.fixture
def preprocessor():
    return SportsImagePreprocessor(target_size=(48, 48))

@pytest.fixture
def sample_pil_image():
    # Create a synthetic 128x128 RGB image with gradient
    arr = np.zeros((128, 128, 3), dtype=np.uint8)
    arr[:, :, 0] = np.linspace(0, 255, 128, dtype=np.uint8)
    arr[:, :, 1] = 120
    arr[:, :, 2] = 200
    return Image.fromarray(arr)

@pytest.fixture
def sample_bgr_frame():
    # Create a synthetic 100x100 BGR numpy array
    return np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)

def test_preprocessor_init(preprocessor):
    assert preprocessor.target_size == (48, 48)
    assert preprocessor.feature_dim == 62

def test_preprocess_pil(preprocessor, sample_pil_image):
    arr = preprocessor.preprocess_pil(sample_pil_image)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (48, 48, 3)
    assert arr.dtype == np.float32
    assert 0.0 <= arr.min() and arr.max() <= 1.0

def test_preprocess_frame_bgr(preprocessor, sample_bgr_frame):
    arr = preprocessor.preprocess_frame(sample_bgr_frame)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (48, 48, 3)
    assert arr.dtype == np.float32

def test_extract_features_shape_and_finite(preprocessor, sample_pil_image):
    feats = preprocessor.extract_features(sample_pil_image)
    assert isinstance(feats, np.ndarray)
    assert feats.shape == (62,)
    assert feats.dtype == np.float32
    assert not np.isnan(feats).any(), "Features must not contain NaNs"
    assert not np.isinf(feats).any(), "Features must not contain Infs"

def test_extract_features_from_bgr_array(preprocessor, sample_bgr_frame):
    feats = preprocessor.extract_features(sample_bgr_frame)
    assert isinstance(feats, np.ndarray)
    assert feats.shape == (62,)

def test_extract_features_invalid_inputs(preprocessor):
    # Non-existent file
    assert preprocessor.extract_features("non_existent_image_12345.png") is None
    # None input
    assert preprocessor.extract_features(None) is None
    # Invalid shape array (2D instead of 3D)
    invalid_arr = np.zeros((50, 50), dtype=np.uint8)
    assert preprocessor.extract_features(invalid_arr) is None

def test_convenience_functions(sample_pil_image, sample_bgr_frame):
    arr_pil = preprocess_pil(sample_pil_image)
    assert arr_pil.shape == (48, 48, 3)

    arr_frame = preprocess_frame(sample_bgr_frame)
    assert arr_frame.shape == (48, 48, 3)
