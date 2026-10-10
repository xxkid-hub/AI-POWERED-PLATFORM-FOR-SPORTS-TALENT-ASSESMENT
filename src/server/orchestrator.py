"""
ApexScout AI - Unified Single-Server Orchestrator
Hosts the complete platform (Web Portal + REST API + AI Inference) on a SINGLE localhost port.
No secondary ports or background servers needed.
"""

import os
import sys
import socket
from .handlers import (
    ApexScoutRequestHandler,
    ThreadedHTTPServer,
    run_server,
    DEFAULT_PORT as DEFAULT_WEB_PORT
)

DEFAULT_PORT = 8000
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def is_port_available(port: int, host: str = "127.0.0.1") -> bool:
    """Checks if a local TCP port is open and available for binding."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5)
        return s.connect_ex((host, port)) != 0


class UnifiedServerOrchestrator:
    """
    Manages the single unified server delivery for all ApexScout AI services
    on one dedicated localhost port.
    """

    def __init__(
        self,
        port: int = DEFAULT_PORT,
        host: str = "0.0.0.0",
        **kwargs
    ):
        self.port = port
        self.host = host
        self.httpd = None

    def start_web_server(self) -> None:
        """Initializes the multi-threaded HTTP server."""
        self.httpd = ThreadedHTTPServer((self.host, self.port), ApexScoutRequestHandler)

    def stop(self) -> None:
        """Gracefully terminates the server."""
        if self.httpd:
            try:
                self.httpd.shutdown()
                self.httpd.server_close()
                print("\n[+] Single Unified Server stopped.", flush=True)
            except Exception as e:
                print(f"[!] Error stopping server: {e}", flush=True)

    def run(self, **kwargs) -> None:
        """Runs the single unified server blocking the main loop."""
        run_server(port=self.port, host=self.host)


def run_unified_server(
    port: int = DEFAULT_PORT,
    web_port: int = None,
    host: str = "0.0.0.0",
    **kwargs
) -> None:
    """Runs the single unified server on the designated localhost port."""
    target_port = web_port if web_port is not None else port
    run_server(port=target_port, host=host)
