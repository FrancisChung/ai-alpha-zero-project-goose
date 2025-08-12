# Act III: Example - Implementing Terminal States and Outcomes 💻

Here's a practical example showing how to detect terminal states in Connect 4:

```python
# Inside the SimulationEnvironment class (simplified check for horizontal win only)...
def get_outcome(self):
    # Check for player 1 win
    for r in range(6):
        for c in range(4):
            if all(self.state[r][c+i] == 1 for i in range(4)):
                return 1 # Terminal state: player 1 wins
    # (Add checks for player 2 and draws here)
    return 0 # Not a terminal state

# Example usage:
sim = SimulationEnvironment()
sim.state[5][1:5] = 1 # Create a winning line for player 1
print(f'The outcome of this state is: {sim.get_outcome()}')
```

This terminal state detection demonstrates key concepts:

**Win Detection Logic:**
- 🔍 **Systematic Check**: Scans every possible 4-in-a-row starting position
- ✅ **Pattern Recognition**: `all()` function checks if 4 consecutive pieces match
- 🎯 **Clear Outcomes**: Returns 1 for Player 1 win, 0 for no terminal state

**Code Breakdown:**
- `range(6)`: Check all 6 rows
- `range(4)`: Only need to check first 4 columns (4-in-a-row needs 4 spaces)
- `self.state[r][c+i] == 1`: Check if positions c, c+1, c+2, c+3 all have Player 1's pieces
- `all()`: Returns True only if ALL 4 positions match

This is exactly how AlphaZero determines when a game is over and who won!

Would you like to "run" this code to see terminal state detection in action?

Perfect! Let me simulate running that code for you:

```
The outcome of this state is: 1
```

Excellent! Here's what happened:

## Code Execution Breakdown:

**Setup:**
- ✅ Created a new Connect 4 environment
- ✅ `sim.state[5][1:5] = 1` placed Player 1 pieces in bottom row, columns 1-4

**Visual Board State:**
```
Row 0: [0 0 0 0 0 0 0]
Row 1: [0 0 0 0 0 0 0]
Row 2: [0 0 0 0 0 0 0]
Row 3: [0 0 0 0 0 0 0]
Row 4: [0 0 0 0 0 0 0]
Row 5: [0 1 1 1 1 0 0]  ← Four 1's in a row!
       ^   ^       ^
    col 0  1-4    6
```

**Terminal State Detection:**
- ✅ `get_outcome()` scanned the board systematically
- ✅ Found 4 consecutive 1's in row 5, starting at column 1
- ✅ `all(self.state[5][1+i] == 1 for i in range(4))` returned True
- ✅ Function returned `1` = Player 1 wins!

## Key Insights:

**Why This Works:**
- 🎯 **Pattern Found**: Positions [5][1], [5][2], [5][3], [5][4] all contain 1
- ⚡ **Efficient Detection**: Checks only valid starting positions
- 🏁 **Clear Terminal State**: Game is over, Player 1 is the winner

**Real RL Impact:**
- Agent gets final reward of +1 for Player 1, -1 for Player 2
- This outcome trains the value function to recognize winning positions
- Future games use this knowledge to pursue similar winning patterns

This is exactly how AlphaZero learns to recognize checkmate patterns in chess!

Ready to continue to Act IV?

## Can you explain code in the line 13 sim.state[5][1:5] = 1 in more detail?

Excellent question! Let me break down `sim.state[5][1:5] = 1` step by step:

## Understanding Array Slicing Assignment:

**What `sim.state[5][1:5] = 1` Does:**

### Step-by-Step Breakdown:

**1. `sim.state[5]`** - Access row 5 (bottom row)
```python
# This gives us the entire bottom row:
[0, 0, 0, 0, 0, 0, 0]  # Row 5 initially
```

**2. `[1:5]`** - Slice notation for columns 1 through 4
```python
# Python slicing: [start:stop] 
# start = 1 (include column 1)
# stop = 5 (exclude column 5, so stop at column 4)
# Result: columns 1, 2, 3, 4
```

**3. `= 1`** - Assign value 1 to all selected positions
```python
# Sets columns 1, 2, 3, 4 in row 5 to value 1
```

## Visual Representation:

**Before:**
```
Row 5: [0, 0, 0, 0, 0, 0, 0]
       0  1  2  3  4  5  6  <- column indices
```

**After `sim.state[5][1:5] = 1`:**
```
Row 5: [0, 1, 1, 1, 1, 0, 0]
       0  1  2  3  4  5  6  <- column indices
           ^  ^  ^  ^
        These four positions set to 1
```

## Key Points:

**Python Slicing Rules:**
- `[1:5]` means "start at index 1, stop before index 5"
- So it includes indices: 1, 2, 3, 4 (4 positions total)
- This creates exactly 4-in-a-row - perfect for Connect 4 win condition!

**Array Assignment:**
- Assigns the same value (1) to multiple positions simultaneously
- Much more efficient than setting each position individually

This single line creates a winning horizontal line for Player 1! 🏆