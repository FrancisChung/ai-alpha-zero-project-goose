# Act III: Example - Model-Based vs Model-Free in Practice 💻

Here's a practical example showing the key difference between these two approaches:

```python
# Model-Based agent: has an internal rulebook
model = {
    'State_A': {
        'action_1': 'State_B'
    }
}
print(f"[Model-Based] I know that taking 'action_1' from 'State_A' leads to 'State_B': {model['State_A']['action_1']}")

# Model-Free agent: learns only through experience
print("[Model-Free] I don't know what happens if I try 'action_1' from 'State_A'... I'll just try it and find out.")
```

This illustrates the fundamental difference:

**Model-Based Agent:**
- Has an internal "rulebook" (the model dictionary)
- Can predict outcomes before acting
- Can plan multiple steps ahead
- Like AlphaZero knowing chess rules

**Model-Free Agent:**
- No internal model of how the world works
- Learns purely through trial and error
- Develops intuitive patterns over time
- Like learning to ride a bike through practice

Your transition function question earlier was perfect - that's exactly what the model-based agent's "rulebook" contains!

Would you like to "run" this code to see how each agent approaches decision-making?