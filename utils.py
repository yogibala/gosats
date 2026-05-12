def calculate_metrics(data):
    btc_percent = (data["btc_earned"] / data["weekly_spend"]) * 100
    # Potential return logic for the 'Proactive Coach'
    potential = data["btc_earned"] * 1.5 
    
    return {
        "btc_percent": round(btc_percent, 2),
        "potential": int(potential),
        "total_wealth_val": data['wealth_assets']['silver_g'] * 85 # Approx INR
    }

def get_mars_signal():
    # Simulated volatility signal for MARS
    return "Market Alert: Silver is up 4%. Suggest swapping 10% BTC rewards to Silver."