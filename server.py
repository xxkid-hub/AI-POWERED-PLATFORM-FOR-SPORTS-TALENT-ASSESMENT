#!/usr/bin/env python3
"""
ApexScout AI - Local Web & API Server
Serves the static web application and provides RESTful endpoints for sports AI assessment,
medical 24h compliance verification, coach discovery, and helpline ticket submission.
"""

import http.server
import socketserver
import os
import json
import urllib.parse
from datetime import datetime
from infer import predict_sports_action

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class ApexScoutRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        if parsed_path.path == '/api/health':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            response = {
                'status': 'HEALTHY',
                'service': 'ApexScout AI Talent Assessment Engine',
                'serverTime': datetime.now().isoformat(),
                'version': '2.4.0'
            }
            self.wfile.write(json.dumps(response).encode('utf-8'))
            return

        elif parsed_path.path == '/api/model-evaluation':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            eval_path = os.path.join(DIRECTORY, 'trained_model', 'evaluation_report.json')
            if os.path.exists(eval_path):
                with open(eval_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            else:
                data = {'status': 'ERROR', 'message': 'No evaluation report found'}
            self.wfile.write(json.dumps(data).encode('utf-8'))
            return
        
        super().do_GET()

    def do_POST(self):
        parsed_path = urllib.parse.urlparse(self.path)
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode('utf-8') if content_length > 0 else '{}'

        try:
            payload = json.loads(post_data)
        except Exception:
            payload = {}

        if parsed_path.path == '/api/verify-medical':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()

            # Mock server validation
            response = {
                'status': 'SUCCESS',
                'verificationToken': 'APEX-MED-SRV-' + str(int(datetime.now().timestamp())),
                'verifiedAt': datetime.now().isoformat(),
                'complianceWindowHours': 24,
                'result': 'PASSED'
            }
            self.wfile.write(json.dumps(response).encode('utf-8'))
            return

        elif parsed_path.path == '/api/predict-sport':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()

            image_path = payload.get('image_path')
            if not image_path:
                image_path = os.path.join(DIRECTORY, 'dataset', 'Cricket', 'CR001 - Copy.png')
                
            prediction = predict_sports_action(image_path)
            self.wfile.write(json.dumps(prediction).encode('utf-8'))
            return

        elif parsed_path.path == '/api/helpline-ticket':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()

            ticket_id = 'TICK-' + str(int(datetime.now().timestamp()))[-6:]
            response = {
                'status': 'DISPATCHED',
                'ticketId': ticket_id,
                'priority': payload.get('urgency', 'URGENT'),
                'dispatchedAt': datetime.now().isoformat()
            }
            self.wfile.write(json.dumps(response).encode('utf-8'))
            return

        self.send_response(404)
        self.end_headers()

def run_server():
    with socketserver.TCPServer(("", PORT), ApexScoutRequestHandler) as httpd:
        print(f"============================================================")
        print(f" ⚡ ApexScout AI - Sports Talent Assessment Platform")
        print(f" Serving locally at: http://localhost:{PORT}")
        print(f" Press Ctrl+C to stop the server.")
        print(f"============================================================")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server gracefully...")

if __name__ == '__main__':
    run_server()
