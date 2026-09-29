"""
Unit tests for the modular Server & REST API endpoints.
"""

import json
from src.server import ApexScoutRequestHandler, DEFAULT_PORT


def test_server_default_port():
    assert DEFAULT_PORT == 8000


def test_handler_class_attributes():
    assert issubclass(ApexScoutRequestHandler, object)
    assert hasattr(ApexScoutRequestHandler, "do_GET")
    assert hasattr(ApexScoutRequestHandler, "do_POST")
    assert hasattr(ApexScoutRequestHandler, "do_OPTIONS")
