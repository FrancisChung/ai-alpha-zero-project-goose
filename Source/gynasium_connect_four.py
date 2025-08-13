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