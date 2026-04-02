import streamlit as st
import pandas as pd
from stable_baselines3 import PPO
from hospital_env import MedicalCloudEnv

# UI Setup
st.set_page_config(page_title="Medical Cloud AI", page_icon="🏥", layout="centered")
st.title("🏥 Medical Cloud AI Orchestrator")
st.markdown("### Autonomous Resource Scaling using Reinforcement Learning")
st.write("Click the button below to see the trained PPO agent manage hospital servers in real-time.")

# Simulation Logic
if st.button("🚀 Run Live Simulation"):
    env = MedicalCloudEnv()
    model = PPO.load("medical_cloud_agent")
    
    obs, _ = env.reset()
    data = []
    
    progress_bar = st.progress(0)
    for i in range(10):
        action, _ = model.predict(obs, deterministic=True)
        obs, reward, _, _, _ = env.step(action)
        servers, uploads = obs
        data.append({"Day": i+1, "Servers": servers, "Uploads": uploads, "Reward": reward})
        progress_bar.progress((i + 1) * 10)

    # Display Results
    df = pd.DataFrame(data)
    st.subheader("Real-Time Decision Logs")
    st.table(df)
    
    st.subheader("Resource Scaling Visualization")
    st.line_chart(df.set_index("Day")[["Servers", "Uploads"]])
    st.success("Simulation successful! The agent optimized server count based on MRI traffic.")
