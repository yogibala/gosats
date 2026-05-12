# data.py
# Simulating the 'Event Collector' payload

USER_DATA = {
    "name": "Rahul",
    "weekly_spend": 6500,
    "btc_earned": 150,
    "partner_ratio": 0.4,
    "wealth_assets": {"silver_g": 10.5, "gold_g": 2.1, "btc_sats": 45000},
    "telemetry": {
        "device_id": "9823-XJ-2026",
        "ip_address": "103.21.154.12",
        "lat_long": (12.9716, 77.5946), # Bengaluru
        "hardware": {
            "ram_gb": 8,
            "is_emulator": False,
            "battery_level": 0.85,
            "screen_res": "1080x2400"
        }
    }
}

# Simulated historical event for geo-velocity calculation
LAST_EVENT = {
    "lat_long": (12.9716, 77.5946), 
    "timestamp": 1715500000 
}