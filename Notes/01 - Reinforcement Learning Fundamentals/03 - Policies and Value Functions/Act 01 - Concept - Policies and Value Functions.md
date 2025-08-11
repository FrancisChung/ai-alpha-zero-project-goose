# Act I: Concept - Policies and Value Functions 🧠

Excellent progress! Now let's explore how agents actually make intelligent decisions.

## The Agent's Decision-Making System

How does an agent decide which action to take? It uses a **Policy**, which is the agent's strategy or "brain." A simple policy might pick actions at random. A smart policy, however, chooses actions that are likely to lead to better long-term outcomes.

To make those decisions, the agent needs to understand not just the *immediate* reward, but the *expected future* reward. This is where the **Value Function** comes in.

- A **Policy** maps a state (or state-action pair) to a chosen action.
- A **Value Function** estimates how good it is to be in a given state (or to take a certain action in that state), based on expected cumulative rewards.

> In simple terms:  
> - The **policy** says *what to do*.  
> - The **value function** says *how good things look from here*.

Together, they allow the agent to plan ahead and act intelligently—not just based on what happened last step, but on what's likely to happen next.

![Policy value function](https://ars.els-cdn.com/content/image/1-s2.0-S2352864825000057-gr002.jpg)

Think of it like this: the policy is your game strategy, and the value function is your ability to evaluate "how winning am I right now?"

Ready to see this in action? Let's continue!