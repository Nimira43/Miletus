# 🧼 Overview of Denoising Noisy Signals

Denoising is the process of **recovering the underlying true signal** from a version that has been corrupted by noise. In real‑world data (neural recordings, audio, sensor measurements, etc.), noise can come from:

- random fluctuations in the environment  
- measurement error  
- biological variability  
- electronic interference  

The goal is to apply a transformation that **reduces noise** while **preserving the important structure** of the original signal.

## 🎯 Core Ideas in Signal Denoising

- **Noise is typically high‑frequency**, random, and unstructured.  
- **True signals are typically smoother**, structured, and correlated over time.  
- A denoising method should reduce noise **without destroying the underlying shape** of the signal.

## Common Denoising Techniques

- **Moving average / mean smoothing**  
  Simple, fast, reduces high‑frequency noise by averaging local neighbourhoods.

- **Median filtering**  
  Good for removing spikes/outliers.

- **Gaussian smoothing**  
  Weighted averaging with a bell‑curve kernel.

- **Fourier‑domain filtering**  
  Remove high‑frequency components directly.

- **Wavelet denoising**  
  Multi‑scale decomposition; very powerful for biological signals.
