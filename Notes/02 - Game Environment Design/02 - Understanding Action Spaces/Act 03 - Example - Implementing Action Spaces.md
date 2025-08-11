# Act III: Example - Implementing Action Spaces 💻

Here's a practical example showing how to implement an action space in a Connect 4-style environment:

```python
# Create a simple Connect 4-style environment
import numpy as np

class SimulationEnvironment:
    def __init__(self):
        # Start with a 6-row, 7-column empty board (like Connect 4)
        self.state = np.zeros((6, 7), dtype=int)
        self.active_player = 1
        print("Environment initialized.")

    def get_action_space(self):
        # An action is valid if the top cell in a column is empty
        return [col for col in range(7) if self.state[0][col] == 0]

# Example usage:
sim = SimulationEnvironment()
sim.state[0][3] = 1  # Block column 3 to simulate a move
print(f"Current Action Space: {sim.get_action_space()}")
```

This example demonstrates key action space concepts:

**Dynamic Action Space:**
- Actions change based on current state
- Only available columns can be selected
- Blocked columns are excluded automatically

**Smart Design:**
- ✅ **Clear Logic**: Top row empty = column available
- ✅ **Efficient**: Returns only valid actions
- ✅ **Realistic**: Matches real Connect 4 rules

This prevents the agent from trying impossible moves and focuses learning on valid strategies!

Would you like to "run" this code to see how the action space changes?

Perfect! Let me simulate running that code for you:

```
Environment initialized.
Current Action Space: [0, 1, 2, 4, 5, 6]
```

Excellent! Here's what happened:

## Code Execution Breakdown:

**1. Environment Setup:**
- ✅ Created a 6×7 Connect 4 board (all zeros = empty)
- ✅ Set active player to 1
- ✅ Printed "Environment initialized."

**2. Simulated Move:**
- ✅ `sim.state[0][3] = 1` - Placed a piece in column 3 (top row)
- ✅ This blocks column 3 from future moves

**3. Action Space Check:**
- ✅ `get_action_space()` returned `[0, 1, 2, 4, 5, 6]`
- ✅ **Notice:** Column 3 is missing! It's blocked.

## Key Insights:

**Dynamic Action Space in Action:**
- **Before move:** Actions would be [0, 1, 2, 3, 4, 5, 6] (all 7 columns)
- **After move:** Actions are [0, 1, 2, 4, 5, 6] (column 3 blocked)

**Why This Matters:**
- 🎯 **Prevents Invalid Moves**: Agent can't try impossible actions
- ⚡ **Faster Learning**: Agent focuses only on valid strategies
- 🔧 **Realistic Simulation**: Matches real game rules

This is exactly how professional RL environments work - they dynamically update available actions based on the current state!

Ready to continue to Act IV?