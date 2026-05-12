# fraud_engine.py

class FraudEngine:
    def __init__(self):
        # Weighted Composite Scoring logic from the architecture diagram
        self.weights = {"rule": 0.6, "anomaly": 0.2, "gen_ai": 0.2} 
        self.blacklisted_fingerprints = ["bot_hash_001", "emulator_v1"]

    def get_rule_score(self, telemetry, amount):
        score = 0
        hw = telemetry['hardware']
        
        # Feature 1: Hardware Entropy & Anomalies
        if hw['is_emulator']: score += 100 
        if hw['ram_gb'] < 2: score += 40
        
        # Feature 2: Canvas/WebGL Fingerprinting
        if hw['canvas_hash'] in self.blacklisted_fingerprints: score += 90
            
        # Feature 3: Transactional Value Velocity
        if amount > 1000000: score += 100 # High-value block
        elif amount > 50000: score += 50   # High-value friction
        
        return min(score, 100)

    def get_location_score(self, present_location, last_location):
        # Feature 4: Simplified Location Anomaly
        # If the user is in a different city than their baseline, flag it
        if present_location != last_location:
            if present_location in ["London", "New York"]: return 95 # Extreme shift
            return 45 # Minor shift (e.g., Delhi vs Bengaluru)
        return 0

    def calculate_risk(self, rule_s, loc_s, gen_ai_s):
        # Rs = (wr * Srule) + (wa * Sanomaly) + (wg * SgenAI)
        return round((rule_s * self.weights['rule']) + 
                     (loc_s * self.weights['anomaly']) + 
                     (gen_ai_s * self.weights['gen_ai']), 2)

    def get_action_tier(self, score):
        # Maps the score to the diagram's action paths
        if score > 80: return "RED - AUTO-BLOCK"
        if score > 40: return "AMBER - FRICTION (OTP/2FA)"
        return "GREEN - ALLOW"