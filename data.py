# data.py
USER_DATA = {
    "name": "Rahul",
    "weekly_spend": 6500,
    "btc_earned": 150,
    "partner_ratio": 0.4,
    "wealth_assets": {"silver_g": 10.5, "gold_g": 2.1, "btc_sats": 45000},
    "last_location": "Bengaluru",
    "telemetry": {
        "device_id": "9823-XJ-2026",
        "ip_address": "103.21.154.12",
        "hardware": {
            "ram_gb": 8,
            "is_emulator": False,
            "screen_res": "1080x2400",
            "canvas_hash": "a1b2c3d4e5", # Simulated unique hardware hash
            "webgl_vendor": "Google Inc. (NVIDIA)"
        }
    }
}

# The 'Baseline' event used for distance comparison
LAST_EVENT = {
    "lat_long": (12.9716, 77.5946), # Bengaluru
    "timestamp": 1715500000 
}