# Medical-Cloud-RL-Orchestrator
Reinforcement Learning agent (PPO) for autonomous cloud resource scaling in healthcare.

---
## 🛠️ How to Run
1. **Clone the repository:**
   `git clone https://github.com`
2. **Install dependencies:**
   `pip install -r requirements.txt`
3. **Train the agent:**
   `python train_agent.py`
4. **Test & Visualize:**
   `python test_and_visualize.py`


## 📊 Performance Results


| Day | Servers | Uploads | Reward |
|-----|---------|---------|--------|
| 1   | 6       | 107     | -2.00   |
| 2   | 7       | 184     | -50.00  |
| 3   | 8       | 175     | -3.00   |
| 4   | 9       | 229     | -50.00  |
| 5   | 10      | 301     | -50.00  |
| 6   | 11      | 335     | -50.00  |
| 7   | 12      | 304     | -50.00  |
| 8   | 13      | 254     | -5.50   |
| 9   | 14      | 293     | -6.00   |
| 10  | 15      | 254     | -6.50   |

### 📝 Key Analysis
The agent successfully learned to prioritize **System Uptime** during high-demand bursts. While it initially struggled with rapid traffic spikes (Days 2-7), it adapted by Day 8 by scaling to **13+ servers**, stabilizing the environment and significantly improving the reward from a crash state (-50.00) to a manageable scaling cost.
