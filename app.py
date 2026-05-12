# app.py
import streamlit as st
import google.generativeai as genai
import os
from data import USER_DATA, LAST_EVENT
from fraud_engine import FraudEngine
from utils import calculate_metrics, get_mars_signal
from prompt import build_prompt

st.set_page_config(page_title="GoSats ANIL Demo", layout="wide")
st.title("GoSats: AI-Native Intelligence Layer (v2.0)")

#
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Transaction Simulation")
    tx_type = st.selectbox("Select Action", ["Buy Voucher", "Swap Silver to BTC", "Withdraw Sats"])
    tx_amount = st.number_input("Amount (INR)", value=2000)
    
    if st.button("Run AI Risk & Wealth Scan"):
        engine = FraudEngine()
        
        # 1. Run Fraud Analysis
        r_score = engine.get_rule_score(USER_DATA['telemetry'])
        a_score = engine.get_anomaly_score(USER_DATA['telemetry']['lat_long'], LAST_EVENT)
        g_score = 10 # Simulated GenAI Intent score
        
        final_score = engine.calculate_risk(r_score, a_score, g_score)
        action = engine.get_action_tier(final_score)
        
        # 2. Display Result with Logic Color
        if "RED" in action: st.error(f"ACTION: {action} (Score: {final_score})")
        elif "AMBER" in action: st.warning(f"ACTION: {action} (Score: {final_score})")
        else: st.success(f"ACTION: {action} (Score: {final_score})")
        
        # 3. AI Insights
        metrics = calculate_metrics(USER_DATA)
        prompt_text = build_prompt(USER_DATA, metrics, final_score)
        
        model = genai.GenerativeModel("gemini-3-flash-preview")
        response = model.generate_content(prompt_text)
        
        with col2:
            st.subheader("ANIL Proactive Insights")
            st.markdown(response.text)
            st.info(get_mars_signal()) #