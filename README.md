# GoSats: AI-Native Intelligence Layer (ANIL) v2.0 Prototype

This repository contains the functional prototype for the **AI-Native Intelligence Layer (ANIL)** and the **Fraud Intelligence Layer**, designed for GoSats' transition into a high-scale wealth platform.

## 🚀 Project Overview
- **Tri-Engine Fraud Analysis:** Real-time risk scoring using Rule, Anomaly, and GenAI engines.
- **Predictive Wealth Coaching:** Proactive Bitcoin and Gold swapping signals (MARS).
- **Dynamic Risk Paths:** Simulated "Allow," "Friction," and "Block" workflows based on behavioral telemetry.

## 🛠️ Architecture Logic
The system is built on a modular "Defense in Depth" strategy:
1. **Event Collection:** Captures "Soft Signal" telemetry including hardware entropy and geo-spatial data.
2. **Contextual Enrichment:** Calculates real-time features like Geo-velocity and Reward Velocity.
3. **Risk Scorer:** A weighted composite engine ($R_s = w_r \cdot S_{rule} + w_a \cdot S_{anomaly} + w_g \cdot S_{genAI}$).
4. **Action Layer:** Automatically routes high-value wealth transactions through Additional Factor Authentication (AFA).

## 📁 File Structure
- `app.py`: The main Streamlit dashboard and UI orchestration.
- `fraud_engine.py`: Core logic for the Rule, Anomaly, and GenAI scoring engines.
- `utils.py`: Wealth metric calculations and Market-Aware Reward Swapping (MARS) signals.
- `data.py`: Simulated user telemetry and historical event baselines.
- `prompt.py`: Structured XML-based prompts for the AI Financial Assistant.

## 🔧 Setup Instructions
1. Clone this repository and install dependencies: `pip install streamlit google-generativeai geopy`.
2. Generate a Google Gemini API key from [Google AI Studio](https://aistudio.google.com/).
3. Set your environment variable: `export GOOGLE_API_KEY='your_key'`.
4. Run the application: `streamlit run app.py`.

## 📊 Success Metrics
- **System Latency:** Designed for <100ms P99 latency in the "Fast Path."
- **Asset Integrity:** Targeted Fraud Loss Rate (FLR) of <0.01% for wealth assets.
- **User Growth:** Optimized for zero-friction rewards tracking to drive MAU growth.

---
*Note: This is a simulation prototype for technical demonstration purposes.*