# app.py
import streamlit as st
import google.generativeai as genai
import os
from data import USER_DATA
from fraud_engine import FraudEngine
from utils import calculate_metrics, get_mars_signal
from prompt import build_prompt

st.set_page_config(page_title="GoSats Intelligence Layer", layout="wide")
st.title("GoSats: AI Fraud & Wealth Engine (Demo v2.1)")

# Configure Gemini for ANIL Insights
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Transaction Simulation")
    tx_amount = st.number_input("Transaction Amount (INR)", value=2000)
    
    # Manual Location Selection for Demo
    present_loc = st.selectbox("Current User Location", 
                               ["Bengaluru", "Delhi", "London", "New York"])

    if st.button("Run AI Risk & Wealth Scan"):
        engine = FraudEngine()
        
        # 1. Execute Logic
        r_score = engine.get_rule_score(USER_DATA['telemetry'], tx_amount)
        l_score = engine.get_location_score(present_loc, USER_DATA['last_location'])
        g_score = 80 if tx_amount > 500000 else 10 # Contextual GenAI weight
        
        final_score = engine.calculate_risk(r_score, l_score, g_score)
        action = engine.get_action_tier(final_score)
        
        # 2. Display Result
        st.metric("Risk Score", f"{final_score}/100")
        if "RED" in action: st.error(action)
        elif "AMBER" in action: st.warning(action)
        else: st.success(action)
        
        # 3. Trigger ANIL Coach
        metrics = calculate_metrics(USER_DATA)
        prompt_text = build_prompt(USER_DATA, metrics, final_score, tx_amount)
        
        model = genai.GenerativeModel("gemini-3.1-flash-lite-preview")
        with col2:
            st.subheader("ANIL Proactive Insights")
            with st.spinner("AI is analyzing..."):
                response = model.generate_content(prompt_text)
                st.markdown(response.text)
                st.info(get_mars_signal())