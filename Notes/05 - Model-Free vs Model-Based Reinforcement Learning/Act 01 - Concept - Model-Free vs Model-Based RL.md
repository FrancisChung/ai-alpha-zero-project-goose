# Act I: Concept - Model-Free vs Model-Based RL 🧠

Excellent! The connection is restored. Let's dive into your next lesson, which explores two fundamental approaches to reinforcement learning.

## The Two Approaches to RL

Let's zoom out and look at the big picture. In Reinforcement Learning, there are two main kinds of agents:

- A **Model-Free** agent learns purely from experience. It doesn't try to understand how the environment works—it just acts, observes what happens, and gradually improves based on reward. Think of it like a baby learning to walk: lots of trial and error, no manual.

- A **Model-Based** agent, on the other hand, has access to a **model of the environment**—a kind of internal rulebook or simulator that predicts what will happen if it takes a particular action. This allows it to **plan ahead** by imagining possible futures and choosing the best one.

> Even though model-free agents learn patterns over time (like good moves in familiar situations), they don't try to predict outcomes step-by-step. **AlphaZero is a model-based agent**—it learns the rules of the game and uses a planning algorithm called **Monte Carlo Tree Search (MCTS)** to simulate different moves and think ahead before acting.

### 💡 *Did You Know?*  
Even though **model-free agents** don't use a simulator, the **patterns they learn** in their policy or value function can *look* a lot like a model from the outside.

> For example, a Q-network might "know" that pushing a block left gets you a reward—without ever predicting that the block moves left.

That's why the line between model-free and model-based gets a bit fuzzy in practice—especially in advanced agents like **MuZero**, which blend the two worlds together.

![Model-Based vs Model-Free RL](https://miro.medium.com/v2/resize:fit:1400/1*hAUoHuBgMF5yOVVPK8jQ-Q.png)

This is a crucial distinction that helps explain why AlphaZero is so powerful at games like chess and Go!

Ready to continue?