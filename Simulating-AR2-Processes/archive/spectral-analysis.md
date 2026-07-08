# 📘 Spectral Analysis — Overview

## 🎯 What Is Spectral Analysis?

Spectral analysis is the study of how the **energy or power** of a signal is distributed across **different frequencies**.  
Instead of looking at a signal in the **time domain** (how it changes over time), spectral analysis looks at it in the **frequency domain** (what frequencies make it up).

It answers questions like:

- *What rhythms exist in my data?*  
- *Which frequencies dominate?*  
- *Is there periodic structure hidden inside noise?*

This is essential in neuroscience, audio processing, physics, engineering, and any domain where signals matter.

---

## 🔍 Why Use Spectral Analysis?

- **Detect periodic patterns** (oscillations, rhythms, cycles)  
- **Identify dominant frequencies**  
- **Filter signals** (remove noise, isolate components)  
- **Understand system dynamics**  
- **Characterise neural activity** (theta, gamma, beta bands, etc.)

---

## 🧠 Time Domain vs Frequency Domain

### Time Domain  

You see the raw signal:  

- spikes
- fluctuations  
- noise  
- trends  

### Frequency Domain  

You see the ingredients:  

- how much **low‑frequency** content  
- how much **high‑frequency** content  
- peaks indicating **strong oscillations**

Spectral analysis is like turning a messy waveform into a clean list of its musical notes.

---

## 📈 Power Spectral Density (PSD)

The **PSD** shows how power is distributed across frequencies.

Common methods:

- **FFT-based periodogram**  
- **Welch’s method** (averaged, smoother PSD)  
- **Multitaper methods** (high‑quality, low‑variance estimates)

---

## 🧪 Common Tools in Python

- `numpy.fft` — Fast Fourier Transform  
- `scipy.signal.welch` — PSD estimation  
- `scipy.signal.spectrogram` — time‑frequency analysis  
- `matplotlib` — plotting spectra  

---

## 🎨 Spectrograms

A **spectrogram** shows how the frequency content changes over time.

It’s a 2D image:

- x‑axis → time  
- y‑axis → frequency  
- colour → power  

Perfect for neural data, audio, or any non‑stationary signal.

---

## 🚀 Fast Fourier Transform (FFT)

The FFT is a fast algorithm for computing the Fourier Transform.

Key points:

- Converts time‑domain samples → frequency bins  
- Complexity drops from \(O(N^2)\) to \(O(N \log N)\)  
- Used everywhere: audio, neuroscience, physics, engineering

---

## 📌 Magnitude and Phase

The FFT gives **complex numbers**.

From each frequency bin:

- **Magnitude** → how strong the frequency is  
- **Phase** → where the sinusoid starts (its alignment)

Often we plot:

\[
|X(f)|^2
\]

which is the **power spectrum**.

---

## 🧠 Fourier Transform in Neural Data

You use it to:

- detect oscillations (theta, beta, gamma)  
- measure rhythmic activity  
- compare conditions  
- build spectrograms  
- feed into PCA/state‑space analysis  
