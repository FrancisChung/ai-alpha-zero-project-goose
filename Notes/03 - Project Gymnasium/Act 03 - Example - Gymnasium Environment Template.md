# Act III: Example - Gymnasium Environment Template 💻

Here's the project template showing how to convert your custom environment to Gymnasium format:

```python
# PROJECT TEMPLATE: Gymnasium Environment Conversion
# Your task: Convert your SimulationEnvironment to this structure

import gymnasium as gym
import numpy as np
from gymnasium import spaces

class GymnasiumConnectFour(gym.Env):
    def __init__(self):
        super().__init__()
        
        # Define action space (7 columns for Connect Four)
        self.action_space = spaces.Discrete(7)
        
        # Define observation space (6x7 board)
        self.observation_space = spaces.Box(
            low=-1, high=1, shape=(6, 7), dtype=np.int8
        )
        
        # Initialize your game state
        self.reset()
    
    def step(self, action):
        # TODO: Implement your transition logic here
        # Must return: (observation, reward, terminated, truncated, info)
        pass
    
    def reset(self, seed=None, options=None):
        # TODO: Reset environment to initial state
        # Must return: (observation, info)
        pass
    
    def render(self, mode='human'):
        # TODO: Optional visualization
        pass

# When you're ready, submit your complete implementation!
```

This template shows the key components you need to implement:

**Gymnasium Standards:**
- 🏗️ **Inherit from `gym.Env`**: Makes it Gymnasium-compatible
- 📏 **Define Spaces**: `action_space` and `observation_space` tell agents what to expect
- 🔄 **Standard Methods**: `step()`, `reset()`, `render()` with specific return formats

**Your Mission:**
- Convert your existing `SimulationEnvironment` logic into this structure
- Implement the `step()` method using your transition function
- Implement the `reset()` method to restart games
- Define proper action and observation spaces

**Key Differences from Your Custom Environment:**
- `step()` returns 5 values: `(observation, reward, terminated, truncated, info)`
- `reset()` returns 2 values: `(observation, info)`
- Spaces are formally defined for agent compatibility

This is your first real project - transforming your custom work into industry-standard format!

Ready to start building?