"""
ApexScout AI - Configuration Package
"""
from .settings import (
    BASE_DIR,
    DATASET_DIR,
    MODEL_DIR,
    RESULTS_DIR,
    CONFIG_DIR,
    SPORTS_CATEGORIES,
    IMG_TARGET_SIZE,
    DEFAULT_SEED,
    TEST_SPLIT,
    SKILL_MAPPING,
    get_config
)

__all__ = [
    "BASE_DIR",
    "DATASET_DIR",
    "MODEL_DIR",
    "RESULTS_DIR",
    "CONFIG_DIR",
    "SPORTS_CATEGORIES",
    "IMG_TARGET_SIZE",
    "DEFAULT_SEED",
    "TEST_SPLIT",
    "SKILL_MAPPING",
    "get_config"
]
