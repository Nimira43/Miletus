# 📘 Gaussian Convolution Smoothing

## 1. 📡 Constructing the Time Axis and Base Signal

Begin by defining a sampling rate:

\[
\text{srate} = 512 \quad \text{samples/second}
\]

This gives a temporal resolution of:

\[
\Delta t = \frac{1}{\text{srate}} = \frac{1}{512} \approx 0.001953 \text{ s}
\]

Then generate a time vector:

```python
time = np.arange(-2, 2 + 1/srate, 1/srate)
```

This produces a symmetric interval:

\[
t \in [-2,\, 2]
\]

with:

\[
N = \frac{4}{\Delta t} \approx 2048 \text{ points}
\]

### The underlying “true” signal

```python
signal = detrend(time**3 + np.sign(time))
```

This combines:

1. A cubic term  
   \[
   f_1(t) = t^3
   \]

2. A discontinuous sign function  
   \[
   f_2(t) = \operatorname{sign}(t) =
   \begin{cases}
   -1 & t < 0 \\
   0 & t = 0 \\
   +1 & t > 0
   \end{cases}
   \]

The sum:

\[
s(t) = t^3 + \operatorname{sign}(t)
\]

is then **detrended**, removing any linear drift:

\[
s_{\text{detrended}}(t) = s(t) - (a t + b)
\]

where \(a, b\) are obtained via least‑squares regression.

### Adding noise

```python
noisysignal = signal + np.random.randn(points) * 1.1
```

This adds Gaussian noise:

\[
n(t) \sim \mathcal{N}(0,\, 1.1^2)
\]

so the observed signal is:

\[
x(t) = s_{\text{detrended}}(t) + n(t)
\]

---

## 2. 🎯 Building the Gaussian Kernel

Define a kernel width:

```python
k = 10
x = np.arange(-k, k + 1) / srate
s = 0.005
```

This creates a small window:

\[
x \in \left[-\frac{10}{512},\, \frac{10}{512}\right]
\approx [-0.0195,\, 0.0195]
\]

with standard deviation:

\[
\sigma = 0.005
\]

### The Gaussian formula

```python
gkern = np.exp(-x**2 / (2 * s**2))
```

This is the continuous Gaussian:

\[
g(x) = \exp\!\left( -\frac{x^2}{2\sigma^2} \right)
\]

In full form:

\[
g(x) = \exp\!\left( -\frac{x^2}{2(0.005)^2} \right)
\]

Note: Here we do **not** normalize the kernel:

\[
\int g(x)\,dx \neq 1
\]

This means the filtered signal will be scaled slightly, but for smoothing purposes this is often fine.

---

## 3. 🔄 Convolution — The Actual Smoothing

The key line:

```python
filtered_signal = np.convolve(noisysignal, gkern, mode='same')
```

implements:

\[
y(t) = (x * g)(t)
\]

where convolution is defined as:

\[
(x * g)(t) = \sum_{\tau=-k}^{k} x(t - \tau)\, g(\tau)
\]

In continuous form:

\[
(x * g)(t) = \int_{-\infty}^{\infty} x(\tau)\, g(t - \tau)\, d\tau
\]

### Why Gaussian convolution smooths

A Gaussian kernel acts as a **low‑pass filter**:

- High‑frequency noise is suppressed  
- Low‑frequency structure (your cubic + sign function) is preserved

The Fourier transform of a Gaussian is also a Gaussian:

\[
\mathcal{F}\{g(x)\} = \exp\!\left( -2\pi^2 \sigma^2 f^2 \right)
\]

Thus frequencies are attenuated according to:

\[
H(f) = e^{-2\pi^2\sigma^2 f^2}
\]

This is a beautifully smooth, monotonic decay — no ripples, no ringing.

---

## 4. 📊 Plotting and Interpretation

We plot:

- The noisy signal  
- The filtered signal  
- The original underlying signal  

This visually demonstrates:

- Noise reduction  
- Preservation of the overall shape  
- Slight smoothing of sharp discontinuities (Gaussian filters blur edges)

---

## 🧠 Summary of What’s Happening

1. **Generate a nonlinear signal** with a discontinuity.  
2. **Add Gaussian noise** to simulate measurement corruption.  
3. **Construct a Gaussian kernel** with width determined by \(k\) and \(\sigma\).  
4. **Convolve** the noisy signal with the kernel to smooth it.  
5. **Plot** everything to show the denoising effect.
