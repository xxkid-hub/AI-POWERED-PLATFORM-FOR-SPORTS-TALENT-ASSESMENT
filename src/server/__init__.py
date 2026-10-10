"""
ApexScout AI - Server Package
Provides the Single Unified Localhost Server for the full platform.
"""

from .handlers import (
    ApexScoutRequestHandler,
    ThreadedHTTPServer,
    run_server,
    DEFAULT_PORT,
)
from .orchestrator import (
    UnifiedServerOrchestrator,
    run_unified_server,
    DEFAULT_WEB_PORT,
    is_port_available,
)

__all__ = [
    "ApexScoutRequestHandler",
    "ThreadedHTTPServer",
    "run_server",
    "run_unified_server",
    "UnifiedServerOrchestrator",
    "DEFAULT_PORT",
    "DEFAULT_WEB_PORT",
    "is_port_available",
]
