# Glossary

## 🧠 **ALM region**

**ALM = Anterior Lateral Motor cortex**  
A part of the mouse brain involved in:

- planning movements  
- preparing actions  
- holding information during delays  

In many experiments, ALM neurons show **ramping activity** when the animal is preparing to move left vs right.

Think of ALM as the mouse’s **“movement‑planning CPU.”**

---

## 📊 **PSTH**

**PSTH = Peri‑Stimulus Time Histogram**
It’s a way to show how a neuron’s firing rate changes around an event (like a cue).

In plain English:
> A PSTH is a smoothed line showing how active a neuron is before, during, and after something happens.

You take spikes → bin them → average across trials → get a clean firing‑rate curve.

---

## 🎭 **Preferred condition**

A neuron often responds more strongly to one condition than another.

Example:

- Cue A → neuron fires a lot  
- Cue B → neuron fires less  

Cue A is the **preferred** condition for that neuron.

In ALM tasks, this is often:

- left vs right cue  
- lick left vs lick right  
- go vs no‑go  

Preferred = “the neuron likes this one.”

---

## 🚫 **Non‑preferred condition**

The opposite.

The condition where the neuron fires **less**.

If Cue A is preferred, Cue B is non‑preferred.

Non‑preferred = “meh, not my favourite.”

---

## 🎯 **Cue‑aligned**

This means you align all trials so that **time zero = cue onset**.

So the x‑axis is:

- negative time = before cue  
- zero = cue  
- positive time = after cue  

This lets you see how neurons respond *relative to the cue*, not absolute clock time.

---

## 📈 **Timeseries (line plot)**

A simple plot where:

- x‑axis = time  
- y‑axis = firing rate  
- each line = one channel / neuron  

This is your spaghetti plot:

- lots of overlapping lines  
- each showing how a neuron’s activity evolves over time  

It’s the rawest, most direct view of population activity.

---

## ⭐ Putting it all together

The file:

**`ALM_PSTH_preferred_cue_timeseries.png`**

means:

> “A line plot showing firing rates over time for ALM neurons, aligned to the cue, for the condition they respond to most strongly.”

And the non‑preferred version is the same but for the weaker condition.

---
