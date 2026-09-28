"""
ApexScout AI - HTTP & REST Request Handlers
Modular request dispatcher for frontend communication and local testing.
"""

import http.server
import socketserver
import os
import json
import urllib.parse
from datetime import datetime
from typing import Dict, Any

DEFAULT_PORT = 8000
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


class ApexScoutRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Handles static web requests and RESTful API calls for ApexScout AI."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=REPO_ROOT, **kwargs)

    def _send_json_response(self, data: Dict[str, Any], status_code: int = 200) -> None:
        """Helper to send JSON response with standard CORS headers."""
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.end_headers()
        self.wfile.write(json.dumps(data, indent=2).encode('utf-8'))

    def do_OPTIONS(self):
        """Respond to preflight requests."""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)

        if parsed.path == '/api/health':
            response = {
                'status': 'HEALTHY',
                'service': 'ApexScout AI Talent Assessment Engine',
                'serverTime': datetime.now().isoformat(),
                'version': '2.4.0'
            }
            self._send_json_response(response, 200)
            return

        elif parsed.path == '/api/model-evaluation':
            eval_path = os.path.join(REPO_ROOT, 'trained_model', 'evaluation_report.json')
            if os.path.exists(eval_path):
                with open(eval_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            else:
                data = {'status': 'ERROR', 'message': 'No evaluation report found'}
            self._send_json_response(data, 200)
            return

        super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode('utf-8') if content_length > 0 else '{}'

        try:
            payload = json.loads(post_data)
        except Exception:
            payload = {}

        if parsed.path == '/api/verify-medical':
            response = {
                'status': 'SUCCESS',
                'verificationToken': f'APEX-MED-SRV-{int(datetime.now().timestamp())}',
                'verifiedAt': datetime.now().isoformat(),
                'complianceWindowHours': 24,
                'result': 'PASSED'
            }
            self._send_json_response(response, 200)
            return

        elif parsed.path == '/api/predict-sport':
            image_path = payload.get('image_path')
            if not image_path:
                image_path = os.path.join(REPO_ROOT, 'dataset', 'Cricket', 'CR001 - Copy.png')

            try:
                from infer import predict_sports_action
                prediction = predict_sports_action(image_path)
            except Exception as e:
                prediction = {
                    'status': 'ERROR',
                    'message': f'Prediction failed: {str(e)}'
                }

            self._send_json_response(prediction, 200)
            return

        elif parsed.path == '/api/helpline-ticket':
            ticket_id = f'TICK-{str(int(datetime.now().timestamp()))[-6:]}'
            response = {
                'status': 'DISPATCHED',
                'ticketId': ticket_id,
                'priority': payload.get('urgency', 'URGENT'),
                'dispatchedAt': datetime.now().isoformat()
            }
            self._send_json_response(response, 200)
            return

        self._send_json_response({'error': 'Not Found', 'path': parsed.path}, 404)


def run_server(port: int = DEFAULT_PORT):
    """Starts the ApexScout HTTP server on the designated port."""
    with socketserver.TCPServer(("", port), ApexScoutRequestHandler) as httpd:
        print("=" * 60)
        print(" ApexScout AI - Sports Talent Assessment Platform")
        print(f" Serving locally at: http://localhost:{port}")
        print(" Press Ctrl+C to stop the server.")
        print("=" * 60)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server gracefully...")
