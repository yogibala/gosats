import streamlit as st
import google.generativeai as genai
import os
from data import USER_DATA
from utils import calculate_metrics
from prompt import build_prompt

# 1. Fetch the API key from environment variables
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("API Key not found. Please set the GOOGLE_API_KEY environment variable.")
    st.stop()

# 2. Configure the SDK
genai.configure(api_key=api_key)

st.title("AI Spend → Wealth Analyzer")

if st.button("Generate Insights"):
    metrics = calculate_metrics(USER_DATA)
    prompt_text = build_prompt(USER_DATA, metrics)

    # 3. Initialize the Gemini 1.5 Flash model
    model = genai.GenerativeModel(
        model_name="gemini-3-flash-preview",
        system_instruction="You are a financial assistant."
    )

    try:
        with st.spinner("Analyzing data..."):
            response = model.generate_content(prompt_text)
            st.markdown(response.text)
            
    except Exception as e:
        st.error(f"Generation failed: {e}")