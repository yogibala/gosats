# utils.py

def calculate_metrics(data):
    """Calculates core wealth and reward metrics for the ANIL coach."""
    # Basic reward math
    btc_percent = (data["btc_earned"] / data["weekly_spend"]) * 100
    
    # Benchmarking logic for the 'Critical Coach' persona
    target_percent = 5.0
    gap = target_percent - btc_percent
    
    # Performance status for the AI prompt logic
    performance = "UNDERPERFORMING" if btc_percent < 3.0 else "OPTIMAL"

    return {
        "btc_percent": round(btc_percent, 2),
        "performance_status": performance,
        "gap_to_elite": round(gap, 2),
        "total_wealth_val": data.get('wealth_assets', {}).get('silver_g', 0) * 85 
    }

def get_mars_signal():
    """Simulates the Market-Aware Reward Swapping (MARS) signal."""
    # In a production environment, this would fetch real-time market volatility
    return "Market Alert: Silver is up 4%. Suggest swapping 10% BTC rewards to Silver for optimal hedge."