import gymnasium as gym
from gymnasium import spaces
import numpy as np

class MedicalCloudEnv(gym.Env):
    def __init__(self):
        super(MedicalCloudEnv, self).__init__()
        # 0: Turn off 1 server, 1: Stay same, 2: Turn on 1 server
        self.action_space = spaces.Discrete(3)
        
        # State: [Current Servers (1-20), Pending MRI Uploads (0-500)]
        self.observation_space = spaces.Box(
            low=np.array([1, 0]), 
            high=np.array([20, 500]), 
            dtype=np.int32
        )
        self.state = np.array([5, 50]) # Start with 5 servers, 50 uploads

    def step(self, action):
        servers, uploads = self.state
        
        if action == 0 and servers > 1: servers -= 1
        elif action == 2 and servers < 20: servers += 1
        
        new_uploads = np.clip(uploads + np.random.randint(-70, 80), 0, 500)
        capacity = servers * 25 
        
        if capacity >= new_uploads:
            # TWEAK: We increased the server cost from 0.05 to 0.25
            # Now, having too many servers will actually result in a negative reward!
            reward = 1.0 - (servers * 0.25) 
        else:
            reward = -20.0 # Double the penalty for a crash
            
        self.state = np.array([servers, new_uploads], dtype=np.int32)
        return self.state, reward, False, False, {}

    def reset(self, seed=None):
        super().reset(seed=seed)
        self.state = np.array([5, np.random.randint(20, 100)], dtype=np.int32)
        return self.state, {}
