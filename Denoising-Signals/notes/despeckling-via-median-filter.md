# 📘 **COMMENTARY.md — Median Filtering & Despeckling - Early Demos**

## 🎯 Overview

These early demos explore how median‑style neighbourhood filtering behaves when applied to a synthetic signal contaminated with random spikes. Unlike Gaussian smoothing, median filtering is **non‑linear**, making it exceptionally effective at removing impulsive noise while preserving edges and underlying structure.

The demos here illustrate:

- How to generate a synthetic “spike‑corrupted” signal  
- How a simple **mean filter** behaves as a baseline  
- Why median filters outperform mean filters for speckle/spike noise  

Later demos will extend this into full median‑filter sweeps, kernel comparisons, and performance evaluation.

---

## #️⃣ **Block 1 — Generating a Spike‑Corrupted Signal**

### ✔ Purpose

To create a controlled test signal containing **salt‑and‑pepper style spikes**, ideal for demonstrating median filtering.

### ✔ Method  

1. **Generate a base signal**  

   ```python
   pnts = 1234
   signal = np.mod(np.linspace(0,5,pnts)**2,5)
   ```

   This produces a smooth, periodic, quadratic‑modulated waveform.

2. **Randomly choose spike locations**  

   ```python
   p = int(0.1*pnts)
   spiketimes = np.random.randint(0,pnts,p)
   ```

   10% of the points become corrupted.

3. **Inject large spikes**  

   ```python
   signal[spiketimes] = np.random.rand(p)*100 + 10
   ```

   These spikes are much larger than the underlying signal, simulating real‑world impulsive noise.

4. **Plot the corrupted signal**  

   ```python
   plt.plot(signal)
   plt.show()
   ```

### ✔ Insight  

This block establishes a noisy testbed where:

- Spikes are **high amplitude**  
- Spikes are **randomly distributed**  
- The underlying signal remains intact  

Perfect for demonstrating the strengths of median filtering.

---

## #️⃣ **Block 2 — Mean Filtering (Baseline Behaviour)**

### ✔ Purpose  

To show how a simple **mean filter** behaves when attempting to remove spike noise.

### ✔ Method  

A sliding window of width `2k` is used:

```python
k = 15

for i in range(pnts):
    signal[i] = np.mean(signal[np.max((0, i-k)):np.min((pnts, i+k))])
```

This replaces each sample with the average of its neighbours.

### ✔ Insight  

Mean filtering is **linear**, which leads to:

- Spikes being **spread out** rather than removed  
- The underlying signal becoming **blurred**  
- Edges being **smoothed away**  
- The filtered signal losing structure  

Mean filters are good for Gaussian noise, but **bad for impulsive noise**.

This block sets the stage for demonstrating why **median filters** are superior for despeckling.
