# 📘 Gaussian Kernel Sweep & Signal Denoising

## 🎯 Overview

This set of demos explores how different Gaussian kernel parameters affect the denoising performance of a noisy 1‑D signal. The workflow systematically varies:

- **Kernel half‑width** (`k`)
- **Gaussian standard deviation** (`σ`)

and evaluates each combination using **Sum of Squared Errors (SSE)** between the filtered signal and the ground‑truth clean signal.

The result is a full **parameter sweep**, visualised as a heatmap, with additional tools for inspecting individual kernels and comparing their shapes.

---

## 🧪 Demo 1 — SSE Grid Over (k, σ)

### Purpose

To evaluate how kernel width and Gaussian spread influence denoising quality.

### Method  

A double loop iterates over:

- `krange = np.arange(3, 303, 20)`  
- `srange = np.linspace(0.001, 0.5, 60)`

For each pair:

1. A Gaussian kernel is generated:

   ```python
   x = np.arange(-k, k+1) / srate
   gkern = np.exp(-x**2 / (2 * σ**2))
   ```

2. The kernel is normalised:

   ```python
   gkern /= sum(gkern)
   ```

3. The noisy signal is filtered:

   ```python
   filtsig = np.convolve(noisysignal, gkern, mode='same')
   ```

4. SSE is computed:

   ```python
   sseMat[ki, si] = np.sum((filtsig - signal)**2)
   ```

### Output  

A heatmap showing SSE across the parameter grid.  
Lower SSE = better denoising.

This visualisation reveals:

- Very small σ → overly sharp kernels → poor smoothing  
- Very large σ → excessive smoothing → signal distortion  
- Optimal region lies in a diagonal band where kernel width and σ are balanced

---

## 🧪 Demo 2 — Storing All Kernels

### Purpose  

To allow inspection of individual Gaussian kernels after the sweep.

### Method  

A parallel structure is created:

```python
allkernels = [[0]*len(srange) for i in range(len(krange))]
```

Each generated kernel is stored:

```python
allkernels[ki][si] = gkern
```

This enables later retrieval:

```python
allkernels[4][2]
```

and plotting:

```python
plt.plot(allkernels[4][2])
```

### Insight  

This is extremely useful for:

- Understanding how kernel shape changes with parameters  
- Debugging unexpected SSE behaviour  
- Teaching Gaussian filtering concepts visually  

---

## 🖼 Demo 3 — Visualising Kernel Shapes

### Purpose  

To compare kernel shapes across different (k, σ) combinations.

### Method  

A 4×4 grid of subplots is created:

- Four evenly spaced `σ` values  
- Four evenly spaced `k` values  

Each subplot displays:

```python
ax[kj, si].plot(allkernels[kidx[kj]][sidx[si]])
```

with titles showing the exact parameters.

### Insight

This grid makes the relationship between kernel width and σ immediately clear:

- Larger `k` → wider kernel support  
- Larger `σ` → flatter, more spread‑out Gaussian  
- Small `σ` + small `k` → sharp, narrow kernels  
- Large `σ` + large `k` → broad, heavy smoothing kernels  

This visualisation is excellent for intuition building.

---

## 📊 Interpretation & Takeaways

### ✔ Gaussian smoothing is highly sensitive to both kernel width and σ  

The SSE heatmap demonstrates that neither parameter can be tuned independently — they interact.

### ✔ Optimal denoising lies in a diagonal band  

This reflects the balance between:

- Enough smoothing to remove noise  
- Not so much smoothing that the signal is distorted

### ✔ Kernel visualisation is essential  

The 4×4 grid makes it easy to see why certain parameter combinations perform poorly.

### ✔ Storing kernels is a smart design choice  

It enables post‑analysis, debugging, and teaching.

---
