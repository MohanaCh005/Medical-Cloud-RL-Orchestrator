Project Architecture: RL-Based Auto-Scaler
The Agent: Proximal Policy Optimization (PPO) implemented via Stable Baselines3.
The Infrastructure: In a production environment, the "Action" (Add/Remove Server) would trigger an AWS Lambda function to update a Kubernetes (K8s) Horizontal Pod Autoscaler.
The Metric: The agent monitors CloudWatch logs (MRI upload traffic) to decide the next scaling action.