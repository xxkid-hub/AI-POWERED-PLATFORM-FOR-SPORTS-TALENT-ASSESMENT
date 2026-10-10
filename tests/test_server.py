"""
Unit tests for the modular Server, REST API endpoints, and Single Unified Server.
"""

from src.server import (
    ApexScoutRequestHandler,
    ThreadedHTTPServer,
    DEFAULT_PORT,
    DEFAULT_WEB_PORT,
    UnifiedServerOrchestrator,
    is_port_available,
)


def test_server_default_ports():
    assert DEFAULT_PORT == 8000
    assert DEFAULT_WEB_PORT == 8000


def test_handler_class_attributes():
    assert issubclass(ApexScoutRequestHandler, object)
    assert hasattr(ApexScoutRequestHandler, "do_GET")
    assert hasattr(ApexScoutRequestHandler, "do_POST")
    assert hasattr(ApexScoutRequestHandler, "do_OPTIONS")
    assert hasattr(ApexScoutRequestHandler, "do_HEAD")


def test_orchestrator_initialization():
    orchestrator = UnifiedServerOrchestrator(port=8088, host="127.0.0.1")
    assert orchestrator.port == 8088
    assert orchestrator.host == "127.0.0.1"
    assert orchestrator.httpd is None


def test_is_port_available_helper():
    result = is_port_available(59999, "127.0.0.1")
    assert isinstance(result, bool)
