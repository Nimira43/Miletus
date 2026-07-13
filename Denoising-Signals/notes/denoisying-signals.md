# 🧠 Denoising Noisy Signals

Below is a clear explanation of each block of the code and how it contributes to the denoising pipeline.

---

## 1. 📡 Generate a Composite Harmonic Signal  

```python
N = 10001
time = np.linspace(0,4*np.pi,N)

signal = np.zeros(N)

for j in range(1,4):
  signal += np.cos(j*time)**j
```

### What this does

- Creates a time axis from \(0\) to \(4\pi\).  
- Builds a synthetic signal by summing nonlinear harmonic components:  
  \[
  \cos(t)^1 + \cos(2t)^2 + \cos(3t)^3
  \]
- This produces a **structured**, smooth, multi‑frequency waveform.

This is your **ground‑truth signal**.

---

## 2. 🌪️ Add Random Noise  

```python
noisysignal = signal + np.random.randn(N)
```

### What this does

- Adds Gaussian noise (mean 0, variance 1).  
- Produces a noisy version that simulates real‑world measurement corruption.

This is the **signal you want to denoise**.

---

## 3. 🧼 Apply a Mean Smoothing Filter  

```python
filtered_signal = copy.deepcopy(noisysignal)

k = 15

for t in range(N):
  lower_bound = np.max((0,t-k))
  upper_bound = np.min((N,t+k))
  filtered_signal[t] = np.mean(noisysignal[lower_bound:upper_bound])
```

### What this does

- For each time index \(t\), you take a window of size \(2k\) around it.  
- You compute the **average** of all noisy samples inside that window.  
- You replace the current sample with that average.

This reduces high‑frequency noise because noise fluctuates rapidly, while the true signal changes more slowly.

### Effect of `k`

- Small `k` → light smoothing, preserves detail  
- Large `k` → heavy smoothing, removes noise but also blurs the signal

---

## 4. 📦 Wrap the Filter in a Function  

```python
def mean_smooth(signalIn, k):
  filtered_signal = copy.deepcopy(signalIn)

  for t in range(N):
    filtered_signal[t] = np.mean(noisysignal[np.max((0,t-k)):np.min((N,t+k))])
  return filtered_signal
```

### What this does

- Encapsulates the smoothing logic into a reusable function.  
- Allows you to test different values of `k` easily.

---

## 5. 📈 Evaluate Denoising Quality Using Correlation  

```python
k_values = np.arange(5, 41)
signal_corrs = []

for k_index in k_values:
  f_signal = mean_smooth(noisysignal, k_index)
  signal_corrs.append(np.corrcoef(f_signal, signal)[0, 1])
```

### What this does

- Loops over many smoothing window sizes.  
- For each `k`, computes the **correlation** between:
  - the filtered signal  
  - the original clean signal  

Correlation close to **1.0** means the filtered signal matches the true signal well.

This gives you a **performance curve** showing how smoothing strength affects signal recovery.

---

## 6. 📊 Plot Correlation vs. Smoothing Window  

```python
plt.plot(k_values, signal_corrs, 'ks-')
```

### What this does

- Produces a curve showing how denoising quality changes with `k`.  
- Typically:
  - correlation rises as noise is removed  
  - then falls again when smoothing becomes too aggressive

This helps you choose the **optimal smoothing window**.

---

## 🎉 Summary

The code implements a full denoising pipeline:

1. **Generate a structured harmonic signal**  
2. **Add Gaussian noise**  
3. **Apply a moving‑average smoothing filter**  
4. **Test multiple smoothing window sizes**  
5. **Measure denoising quality using correlation**  
6. **Plot the results to find the best `k`**

It’s a clean, intuitive introduction to signal denoising — and a great foundation for more advanced methods like Gaussian filtering, Savitzky–Golay, Fourier filtering, or wavelet denoising.
