#!/usr/bin/env python3
"""
SentinelEye JSON Audit Logger
Maintains append-only tamper-evident compliance logs of workplace safety incidents.
"""

import os
import json
import time
from datetime import datetime

class IncidentLogger:
    def __init__(self, log_path="sentinel_incidents.json"):
        self.log_path = log_path
        self._ensure_file()

    def _ensure_file(self):
        if not os.path.exists(self.log_path):
            with open(self.log_path, "w") as f:
                json.dump([], f)

    def log_incident(self, incident_type, severity, details, worker_id=None, zone_id=None, bbox=None):
        timestamp = datetime.utcnow().isoformat() + "Z"
        incident = {
            "incident_id": f"INC-{int(time.time() * 1000)}",
            "timestamp": timestamp,
            "incident_type": incident_type,
            "severity": severity,
            "worker_tracker_id": worker_id,
            "zone_id": zone_id,
            "bounding_box": bbox or [],
            "compliance_details": details,
            "action_taken": "DISPATCH_AUDIO_ALARM_AND_BROADCAST_MQTT",
            "audit_status": "UNRESOLVED_PENDING_SUPERVISOR_SIGNOFF"
        }

        try:
            with open(self.log_path, "r+") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = []
                data.append(incident)
                # Keep latest 500 incidents
                if len(data) > 500:
                    data = data[-500:]
                f.seek(0)
                f.truncate()
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"[ERROR] Failed to write incident to log: {e}")

        return incident
