def calculate_metrics(data):
    btc_percent = (data["btc_earned"] / data["weekly_spend"]) * 100
    potential = data["btc_earned"] * 1.5

    return {
        "btc_percent": round(btc_percent, 2),
        "potential": int(potential)
    }