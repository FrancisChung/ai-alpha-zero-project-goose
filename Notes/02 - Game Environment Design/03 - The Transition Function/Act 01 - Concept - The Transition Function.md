# Act I: Concept - The Transition Function 🔄

Excellent! Now let's explore how environments actually respond to agent actions.

## From Action to Consequence

So, your agent has made a choice from its action space. Now what?

Imagine you are playing chess. You move your queen to a new square. When you do that:
- The piece moves
- The board updates
- Maybe you capture an opponent's piece
- Maybe the game ends

That chain reaction — from **action** to **consequences** — is what we call the **Transition Function**.

In reinforcement learning, the transition function is the "physics engine" of your environment. It's the system that takes:

> `current_state + action → next_state`

**This is where your simulation comes alive.**

## Key Insights:

**Remember from your RL Fundamentals:** You learned about transition functions as the "rulebook" that model-based agents use for planning!

**Connection to AlphaZero:** When AlphaZero simulates moves during MCTS, it's using the game's transition function to predict what the board will look like after each possible move.

**Why This Matters:**
- ✅ **Deterministic Games**: Chess, Connect 4 - same action always produces same result
- 🎲 **Stochastic Games**: Poker, real-world scenarios - outcomes have probabilities
- 🏗️ **Environment Design**: This is where you implement the actual game rules!

Ready to see how we implement this crucial component?