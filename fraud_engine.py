# fraud_engine.py

class FraudEngine:
    def __init__(self):
        # UPDATE: Increased Anomaly weight to 0.5 to make location matter more
        self.weights = {"rule": 0.3, "anomaly": 0.5, "gen_ai": 0.2} 
        self.blacklisted_fingerprints = ["bot_hash_001", "emulator_v1"]

    def get_rule_score(self, telemetry, amount):
        score = 0
        hw = telemetry['hardware']
        if hw['is_emulator']: score += 100 
        if hw['ram_gb'] < 2: score += 40
        if hw['canvas_hash'] in self.blacklisted_fingerprints: score += 90
        
        # Rule: Extreme Amount check
        if amount > 1000000: score += 100 
        elif amount > 50000: score += 50
        return min(score, 100)

    def get_location_score(self, present_location, last_location):
        # UPDATE: Higher scores for location shifts
        if present_location != last_location:
            # If shift is to New York/London, return 180 to force a 'RED' block
            if present_location in ["London", "New York"]: return 90 
            return 80 
        return 0

    def calculate_risk(self, rule_s, loc_s, gen_ai_s):
        # Weighted Composite Score
        return round((rule_s * self.weights['rule']) + 
                     (loc_s * self.weights['anomaly']) + 
                     (gen_ai_s * self.weights['gen_ai']), 2)

    def get_action_tier(self, score):
        if score > 80: return "RED - AUTO-BLOCK (Identity Theft Suspected)"
        if score > 40: return "AMBER - FRICTION (Location Mismatch)"
        return "GREEN - ALLOW"