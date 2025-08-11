# Act III: Example - Building a Game Environment Class 💻

Here's a practical example showing how to start building a game environment using Python classes:

```python
import numpy as np

class SimulationEnvironment:
    def __init__(self):
        # The initial conditions of our simulation
        self.state = np.zeros((6, 7), dtype=int)
        self.active_player = 1
        print('New SimulationEnvironment instance created.')

sim = SimulationEnvironment()
print(f'Initial state is a board of shape: {sim.state.shape}')
```

This example demonstrates the key principles:

**Class Structure:**
- `__init__()` method sets up the initial state
- `self.state` represents the game board (6x7 grid - looks like Connect 4!)
- `self.active_player` tracks whose turn it is
- Each instance is independent and isolated

**Why This Works:**
- ✅ **Repeatable**: Every new instance starts the same way
- ✅ **Isolated**: Multiple games can run simultaneously
- ✅ **Organized**: All game logic contained in one class
- ✅ **Scalable**: Can create thousands of instances for training

This is exactly the foundation AlphaZero needs to play millions of games!

Would you like to "run" this code to see how the environment gets created?

Perfect! Let me simulate running that code for you:

```
New SimulationEnvironment instance created.
Initial state is a board of shape: (6, 7)
```

Excellent! Here's what happened:

## Code Execution Breakdown:

**1. Environment Creation:**
- ✅ `SimulationEnvironment()` was called
- ✅ `__init__()` method executed automatically
- ✅ Created a 6x7 board filled with zeros (empty spaces)
- ✅ Set active_player to 1 (player 1 starts)

**2. Output Analysis:**
- **"New SimulationEnvironment instance created."** - Confirms the class instantiation
- **"Initial state is a board of shape: (6, 7)"** - Shows we have a 6 rows × 7 columns grid

## What This Represents:
This looks like a **Connect 4** environment setup!
- 6 rows, 7 columns = classic Connect 4 board
- `np.zeros()` means all positions start empty (value 0)
- Player 1 and Player 2 can place pieces (values 1 and 2)

## Key Benefits Demonstrated:
- 🔄 **Fresh Start**: Each instance begins with clean state
- 🏗️ **Structure**: Game state and rules are organized
- 🎯 **Ready for AI**: Agent can interact with this environment
- 📈 **Scalable**: Can create thousands for parallel training

This is exactly how environments are built for training AI agents like AlphaZero! The agent will call methods on this class to make moves and receive feedback.

Ready to continue to Act IV?