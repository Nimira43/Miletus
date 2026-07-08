# 📘 Fourier Transform — Explained

## 🎯 What Is the Fourier Transform?

The **Fourier Transform (FT)** decomposes any signal into a sum of **sinusoids** (sines and cosines) of different frequencies.

It answers:

> **What frequencies are present in my signal, and how strong are they?**

Mathematically, it transforms a function from the **time domain** into the **frequency domain**.

---

## 🧮 The Core Equation

\[
X(f) = \int_{-\infty}^{\infty} x(t)\, e^{-i 2\pi f t}\, dt
\]

Where:

- \(x(t)\) — original signal  
- \(X(f)\) — frequency representation  
- \(e^{-i 2\pi f t}\) — complex sinusoid  
- \(f\) — frequency  

This equation says:

> Multiply your signal by a sinusoid of frequency \(f\), integrate, and you get how much of that frequency exists in the signal.

---

## ⚡ Intuition (The Important Bit)

Think of the Fourier Transform as a **frequency scanner**:

- It tries every possible frequency  
- Measures how strongly that frequency appears in the signal  
- Stores the result in \(X(f)\)

If the signal contains a strong oscillation at 40 Hz, the FT will show a **big peak at 40 Hz**.
