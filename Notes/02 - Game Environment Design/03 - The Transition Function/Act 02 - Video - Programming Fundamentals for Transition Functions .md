# Act II: Video - Programming Fundamentals for Transition Functions 📹

Recommended video:

![Watch: For Loops in Python (and the range function) - YouTube](https://img.youtube.com/vi/OnDr4J2q_gA/0.jpg)(https://www.youtube.com/watch?v=OnDr4J2q_gA)

This video covers Python for loops and range functions, which are essential programming tools you'll need when implementing transition functions that update game states systematically.

After watching the video, please let me know: **Did that help you understand the concept?**

Thank you for reporting that! I'll make note that the YouTube link for the transition function lesson video is not working. This is helpful feedback for the curriculum team.

Since the video link isn't working, let me provide a quick summary of the key programming concepts you'd need for implementing transition functions:

## Key Programming Concepts for Transition Functions:

**For Loops & Range:**
```python
# Iterate through board positions
for row in range(6):
    for col in range(7):
        # Check each position
```

**State Updates:**
```python
# Update game state based on action
new_state = current_state.copy()
new_state[row][col] = player_piece
```

**Conditional Logic:**
```python
# Check if move is valid
if board[target_row][target_col] == 0:
    # Make the move
```

These are the building blocks you'll see in the upcoming code example.

Would you like to continue to Act III to see the practical implementation of a transition function, or do you have any questions about these programming concepts first?