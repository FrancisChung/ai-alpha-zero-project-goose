Fantastic question, Francis! **Rewards** are absolutely critical - they're how the agent learns what "success" looks like. Let me break this down:

## Purpose of Rewards in the Loop:

**1. Learning Signal** 📡
- Rewards tell the agent "this action/state was good/bad"
- Without rewards, the agent has no idea how to improve
- It's like learning without any feedback - impossible!

**2. Goal Definition** 🎯
- Rewards define what the agent should optimize for
- They encode the human designer's intentions
- Whatever gets rewarded is what the agent will try to maximize

**3. Behavior Shaping** 🏗️
- Positive rewards reinforce good behavior
- Negative rewards (penalties) discourage bad behavior
- The agent gradually learns to seek high-reward states/actions

## Commonly Used Reward Functions:

### **1. Sparse Rewards** 🎯
```python
# Chess/Go example:
reward = {
    +1: "win the game",
     0: "draw", 
    -1: "lose the game",
     0: "every other move"  # No reward during play
}
```
**Pros**: Clear, unambiguous goal  
**Cons**: Very hard to learn from (like only getting grades at end of semester)

### **2. Dense Rewards** 🌊
```python
# Robot navigation:
reward = {
    +10: "reach target",
    +1:  "move closer to target",
    -1:  "move away from target",
    -5:  "hit obstacle",
    -0.1: "each step taken" # Time penalty
}
```
**Pros**: Constant feedback, faster learning  
**Cons**: Risk of reward hacking, hard to design well

### **3. Shaped Rewards** ⚡
```python
# Game playing with hints:
reward = {
    +100: "win game",
    +10:  "capture enemy piece", 
    +5:   "control center of board",
    +1:   "develop pieces early",
    -50:  "lose game"
}
```

### **4. Curiosity/Exploration Rewards** 🔍
```python
# Encourage exploration:
reward = {
    +1: "visit new state never seen before",
    +0.1: "take action that increases knowledge"
}
```

### **5. Multi-Objective Rewards** ⚖️
```python
# Autonomous driving:
total_reward = (
    -10 * crashes + 
    +5 * distance_traveled +
    -1 * time_taken +
    -2 * passenger_discomfort
)
```

## Real-World Example - AlphaZero:
AlphaZero uses **sparse rewards**:
- +1 for winning
- 0 for draw  
- -1 for losing
- 0 for all moves during the game

This seems simple, but it's actually genius! It lets AlphaZero discover its own evaluation criteria rather than being biased by human-designed intermediate rewards.

## The Reward Design Challenge:
**"Be careful what you reward - you might get it!"**

Bad example:
```python
# Intended: Make robot move fast
reward = +1 * speed

# Actual result: Robot spins in circles at maximum speed! 🤦‍♂️
```

Better design:
```python
# Actually reward progress toward goal
reward = +1 * (distance_to_goal_decreased) + +10 * (reached_goal)
```

Which type of reward function sounds most intuitive to you for learning? Can you think of how you'd reward an AI learning to play a sport?