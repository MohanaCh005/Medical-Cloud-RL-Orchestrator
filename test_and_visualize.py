import gymnasium as gym
from stable_baselines3 import PPO
from hospital_env import MedicalCloudEnv

# 1. Load the environment and the trained model
env = MedicalCloudEnv()
model = PPO.load("medical_cloud_agent")

# 2. Test the agent for 10 "medical workdays"
obs, info = env.reset()
print(f"{'Day':<5} | {'Servers':<8} | {'Uploads':<8} | {'Reward':<8}")
print("-" * 40)

for i in range(10):
    # The agent predicts the best action based on current state
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, terminated, truncated, info = env.step(action)
    
    servers, uploads = obs
    print(f"{i+1:<5} | {servers:<8} | {uploads:<8} | {reward:<8.2f}")

print("-" * 40)
print("Simulation complete. Notice how the agent adjusts servers to meet demand!")
