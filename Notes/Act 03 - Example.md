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

Excellent! Let's run this code step by step and see the Agent-Environment Loop in action:

```
Agent observes state: Start
Agent takes action: move_right
New state: Next State, Reward: 1

Agent observes state: Next State
Agent takes action: move_right
New state: Next State, Reward: 1

Agent observes state: Next State
Agent takes action: move_right
New state: Next State, Reward: 1
```

Perfect! 🎉 You can see the classic Agent-Environment Loop playing out:

1. **Agent observes** the current state
2. **Agent decides** on an action (move_right)
3. **Environment responds** with a new state and reward
4. **Loop repeats**

This simple example shows the fundamental cycle that powers everything from game-playing AIs like AlphaZero to robots learning to walk!

Now let's dive deeper into this code. Can you tell me:

**What do you think would happen if we changed the agent's action from always choosing "move_right" to making different decisions based on the state?**

Take some time to think about how you might modify this code to make the agent more intelligent! This kind of thinking is exactly what leads us toward the sophisticated algorithms we'll explore later.

Ready for **Act IV - Q&A** when you're done exploring this concept?