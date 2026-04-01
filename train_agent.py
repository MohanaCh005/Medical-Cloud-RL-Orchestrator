from stable_baselines3 import PPO
from hospital_env import MedicalCloudEnv

# 1. Initialize the environment
env = MedicalCloudEnv()

# 2. Define the Agent (MlpPolicy = Multi-layer Perceptron, aka Neural Network)
model = PPO("MlpPolicy", env, verbose=1)

# 3. Start Training (Let it play 10,000 rounds of the "Cloud Game")
print("Training the agent... This will take a minute.")
model.learn(total_timesteps=10000)

# 4. Save the "Brain"
model.save("medical_cloud_agent")
print("Model saved! Ready to test.")
