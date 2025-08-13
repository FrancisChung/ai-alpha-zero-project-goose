# PROJECT TEMPLATE: Gymnasium Environment Conversion
# Your task: Convert your SimulationEnvironment to this structure

import gymnasium as gym
import numpy as np
from gymnasium import spaces
from math import random


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
        self.board = None
        self.current_player = None
        self.reset()

    def step(self, action):
        # 1. Apply the action (drop piece)
        # 2. Check if game ended
        # 3. Switch players
        # 4. Calculate reward
        # 5. Return (observation, reward, terminated, truncated, info)


        # TODO: Implement your transition logic here
        # Must return: (observation, reward, terminated, truncated, info)
        pass

    def transition(self, action_col):
        for r in range(5, -1, -1):
            if self.state[r][action_col] == 0:
                self.state[r][action_col] = self.active_player
                break
        self.active_player *= -1

    def win_outcome_horizontal(self, player_num: int):
        # Check for player 1 win
        for r in range(6):
            for c in range(4):
                if all(self.state[r][c + i] == player_num for i in range(4)):
                    return 1  # Terminal state: player 1 wins
        # (Add checks for player 2 and draws here)
        return 0  # Not a terminal state

    def win_outcome_vertical(self, player_num: int):
        # Check for player 1 win
        for c in range(4):
            for r in range(6):
                if all(self.state[r][c + i] == player_num for i in range(4)):
                    return 1  # Terminal state: player 1 wins
        # (Add checks for player 2 and draws here)
        return 0  # Not a terminal state

    def reset(self, seed=None, options=None):
        # TODO: Reset environment to initial state
        self.board = np.zeros((6,7), dtype = np.int8) #col, row
        self.current_player = 1
        return self.board.copy(), {}


    def render(self, mode='human'):
        # TODO: Optional visualization
        pass

    def simulate_trajectory(env):
        trajectory = []
        outcome = 0

        while outcome == 0:
            # In practice, the agent would choose an action based on a policy
            # Here, we choose randomly from valid options
            action = random.choice(env.get_action_space())

            # Capture the state before the action
            state_snapshot = env.state.copy()

            # Apply the action and transition to a new state
            env.transition(action)

            # Get the outcome (0 if still running, +1 or -1 if terminal)
            outcome = env.get_outcome()

            # Record this step in the trajectory
            trajectory.append({'state': state_snapshot, 'action': action})

        print(f"Trajectory complete: {len(trajectory)} steps. Final outcome: {outcome}")
        return trajectory

# When you're ready, submit your complete implementation!