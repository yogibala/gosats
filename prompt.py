def build_prompt(data, metrics):
    return f"""
User Name: {data['name']}
Weekly Spend: ₹{data['weekly_spend']}
Bitcoin Earned: ₹{data['btc_earned']}
Reward %: {metrics['btc_percent']}%
Partner Spend Ratio: {data['partner_ratio']}

Instructions:
- Explain value clearly
- Suggest improvement
- Keep under 100 words
- Output:
  Summary:
  Insight:
  Actions:
"""