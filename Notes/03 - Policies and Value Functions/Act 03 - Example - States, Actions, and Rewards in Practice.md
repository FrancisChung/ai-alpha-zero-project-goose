# Act III: Example - States, Actions, and Rewards in Practice 💻

Here's a simple example showing how these three elements work together in a chess scenario:

```python
# we are logging what we observed, did, and received.
state = "Chessboard: Agent's knight at G1, opponent's pawn at F3"
action = "Move knight to F3"
reward = 1  # Agent captures a pawn

# Log the experience
print("=== Agent Experience ===")
print(f"State: {state}")
print(f"Action taken: {action}")
print(f"Reward received: {reward}")
```

This code demonstrates the core cycle:
1. **State**: The agent observes the current chess position
2. **Action**: The agent decides to move its knight to capture a pawn
3. **Reward**: The environment gives positive feedback (+1) for capturing the opponent's piece

Would you like to "run" this code to see how the agent logs its experience?