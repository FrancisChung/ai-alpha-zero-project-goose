# Act III - Example 💻

Perfect! Now let's see the Agent-Environment Loop in action with a hands-on Python example.

Here's a simple implementation that demonstrates the core concepts:

```python
class Environment:
    def __init__(self):
        self.state = "Start"

    def step(self, action):
        print(f"Agent takes action: {action}")
        self.state = "Next State"
        reward = 1  # Simplified reward
        return self.state, reward

class Agent:
    def act(self, state):
        print(f"Agent observes state: {state}")
        return "move_right"  # Dummy action

# Simulation
env = Environment()
agent = Agent()

state = env.state
for t in range(3):
    action = agent.act(state)
    state, reward = env.step(action)
    print(f"New state: {state}, Reward: {reward}\n")
```

Would you like to "run" this code to see the Agent-Environment Loop in action? This will help you understand how the agent observes states, takes actions, and receives feedback from the environment! 🚀