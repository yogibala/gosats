# fraud_engine.py
# Logic for the Anomaly, Rule, and GenAI engines

import time

class FraudEngine:
    def __init__(self):
        self.weights = {"rule": 0.5, "anomaly": 0.3, "gen_ai": 0.2} #

    def get_rule_score(self, telemetry):
        # Deterministic check: Is it an emulator or low RAM?
        if telemetry['hardware']['is_emulator'] or telemetry['hardware']['ram_gb'] < 2:
            return 100
        return 0

    def get_anomaly_score(self, current_geo, last_event):
        # Simulated Geo-velocity: Did they travel 1000km in 1 min?
        # In a real app, use geopy.distance.geodesic
        return 15 # Normal behavior simulated

    def calculate_risk(self, rule_s, anomaly_s, gen_ai_s):
        # Weighted Composite Score
        composite = (rule_s * self.weights['rule']) + \
                    (anomaly_s * self.weights['anomaly']) + \
                    (gen_ai_s * self.weights['gen_ai'])
        return round(composite, 2)

    def get_action_tier(self, score):
        # Tiered Logic from the Diagram
        if score > 80: return "RED - BLOCK"
        if score > 40: return "AMBER - FRICTION (OTP)"
        return "GREEN - ALLOW"