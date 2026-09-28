"""
ApexScout AI - Server Package
Provides HTTP and RESTful API endpoints for the web frontend,
including prediction routing, medical SLA verification, and helpline ticketing.
"""

from .handlers import (
    ApexScoutRequestHandler,
    run_server,
    DEFAULT_PORT,
)

__all__ = [
    "ApexScoutRequestHandler",
    "run_server",
    "DEFAULT_PORT",
]
