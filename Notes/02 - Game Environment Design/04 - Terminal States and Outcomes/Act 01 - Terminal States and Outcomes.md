# Act I: Concept - Terminal States and Outcomes 🏁

Excellent! Now let's explore how games end and agents learn from their final results.

## When the Game Ends

Imagine playing a game that *never ends*. No winning. No losing. Just… endless moves.

For an AI agent, this is a nightmare. Without a way to say **"the episode is over"**, it has no feedback on whether it did well or failed.

In reinforcement learning, a **Terminal State** is any situation where the simulation stops — like a checkmate in chess, a full board in Connect 4, or even a crash in a robotics simulator.

But it's not enough to just stop. We also give the agent an **Outcome**: a final reward that says:

- ✅ *You succeeded!* (+1)
- ❌ *You failed.* (–1)
- 🤷 *It's a draw.* (0)

This is the **lesson** the agent carries forward.

## Why This Matters:

**Connection to Your RL Knowledge:**
- Remember **rewards** from your fundamentals? Terminal rewards are the most important ones!
- **Exploration vs Exploitation**: Agents need clear outcomes to know what worked
- **Value Functions**: Terminal rewards help agents learn to evaluate positions

**For AlphaZero:**
- Each game ends with a clear win/loss/draw
- These outcomes train the value network to predict "how likely am I to win from here?"
- Without terminal states, AlphaZero couldn't learn what constitutes good play!

Ready to see how we implement this crucial component?