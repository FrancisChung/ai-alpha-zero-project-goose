# Act III: Example - Implementing a Transition Function 💻

Here's a practical example showing how to implement a transition function for Connect 4:

```python
# Inside the SimulationEnvironment class...
def transition(self, action_col):
    # Drop a piece into the selected column for the current player
    for r in range(5, -1, -1):
        if self.state[r][action_col] == 0:
            self.state[r][action_col] = self.active_player
            break
    # Switch the active player (-1 ↔ 1)
    self.active_player *= -1

# Example usage:
sim = SimulationEnvironment()
print('State before transition:')
print(sim.state)
sim.transition(3)
print('\nState after transition:')
print(sim.state)
```

This transition function demonstrates key concepts:

**Physics Engine in Action:**
- 🔄 **State Update**: `current_state + action → next_state`
- 🏃 **Gravity Simulation**: Piece drops to lowest empty row
- 🔀 **Turn Switching**: Player 1 → Player -1 → Player 1...

**Programming Breakdown:**
- `range(5, -1, -1)` = counts down from row 5 to row 0 (bottom to top)
- `self.state[r][action_col] == 0` = finds first empty slot
- `self.active_player *= -1` = switches between 1 and -1

This is exactly how AlphaZero's environment processes moves during training and MCTS planning!

Would you like to "run" this code to see the state transition in action?

Perfect! Let me simulate running that code for you:

```
State before transition:
[[0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]]

State after transition:
[[0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 1 0 0 0]]
```

Excellent! Here's what happened:

## Transition Function in Action:

**Before Transition:**
- ✅ Empty 6×7 board (all zeros)
- ✅ Active player = 1

**Action Taken:**
- ✅ `sim.transition(3)` - Drop piece in column 3

**After Transition:**
- ✅ **Gravity Effect**: Piece dropped to bottom row (row 5, column 3)
- ✅ **State Update**: `[5][3] = 1` (Player 1's piece placed)
- ✅ **Player Switch**: Active player changed from 1 to -1

## Key Insights:

**Physics Engine Working:**
- 🎯 **Realistic Behavior**: Piece falls to bottom due to gravity
- ⚡ **Efficient Search**: Loop finds lowest empty slot quickly
- 🔄 **Clean State Update**: Board reflects the move accurately

**Connect 4 Rules Implemented:**
- Column 3 now has a Player 1 piece at the bottom
- Next move will be Player -1's turn
- Future pieces in column 3 will stack on top

This is exactly how AlphaZero processes moves - clean, deterministic state transitions that perfectly simulate the game rules!

Ready to continue to Act IV?

## Can you explain what each of the elements represent in range(5, -1, -1) in line 4 of the code example

Excellent question! Let me break down `range(5, -1, -1)` step by step:

## Understanding range(5, -1, -1):

The `range()` function in Python takes three parameters:
```python
range(start, stop, step)
```

### Breaking Down Each Element:

**First Element: `5` (start)**
- Start counting from 5
- This is row 5 (the bottom row of our 6-row board)

**Second Element: `-1` (stop)**
- Stop BEFORE reaching -1
- Since we're counting backwards, this means stop after reaching 0
- So we'll visit: 5, 4, 3, 2, 1, 0

**Third Element: `-1` (step)**
- Count backwards by 1 each time
- Negative step means we go in reverse direction

## What This Produces:
```python
list(range(5, -1, -1))  # [5, 4, 3, 2, 1, 0]
```

## Why This Works for Connect 4:

**Board Layout (6 rows, indexed 0-5):**
```
Row 0: [0 0 0 0 0 0 0]  ← Top row
Row 1: [0 0 0 0 0 0 0]
Row 2: [0 0 0 0 0 0 0]
Row 3: [0 0 0 0 0 0 0]
Row 4: [0 0 0 0 0 0 0]
Row 5: [0 0 0 0 0 0 0]  ← Bottom row (where pieces should land)
```

**Gravity Simulation:**
- Start checking from row 5 (bottom)
- Move upward through rows 4, 3, 2, 1, 0
- Place piece in first empty slot found
- This simulates a piece "falling down" due to gravity!

So `range(5, -1, -1)` elegantly implements the physics of dropping a Connect 4 piece!

