# State‑Space Trajectories & PCA

## 1) **What we’re actually analysing**

We have **many neurons**, each firing over **many timepoints**.

At each moment, the brain is in a “state”:

```md
state(t) = [neuron1(t), neuron2(t), ..., neuronN(t)]
```

This is a **point in N‑dimensional space**.

As time moves, that point **moves** → a *trajectory*.

---

## 2) **Why PCA exists**

Neural data is huge (50–300 dimensions).  
Humans can only visualise **2D or 3D**.

PCA compresses the data while keeping the important structure:

- PC1 = strongest pattern  
- PC2 = second strongest  
- PC3 = third strongest  

Now we can plot:

```md
[PC1(t), PC2(t), PC3(t)]
```

This is our **state‑space trajectory**.

---

## 3) **What PCA actually does**

PCA finds:

- directions where neurons vary together  
- axes that explain the most variance  
- the “shape” of the neural population activity  

It’s like rotating the data so the important patterns line up with the axes.

---

## 4) **What a neural trajectory *means***

A trajectory shows:

- how the brain moves from one cognitive state to another  
- how different conditions separate (preferred vs non‑preferred)  
- how stable or unstable the dynamics are  
- how the population evolves over time  

It’s the brain’s **internal movie**.

---

## 5) **The workflow (start to finish)**

### **A) Load & inspect**

- Load `.mat`  
- Print shapes  
- Plot heatmaps  
- Check for dead channels  

### **B) Clean**

- Remove bad channels  
- Smooth firing rates  
- Z‑score or normalise  
- Align trials  

### **C) Prepare for PCA**

Shape must be:

```md
(timepoints, channels)
```

### **D) Run PCA**

- Fit PCA  
- Transform data  
- Extract PC1, PC2, PC3  

### **E) Plot trajectory**

- 2D: PC1 vs PC2  
- 3D: PC1 vs PC2 vs PC3  
- Compare conditions  

---

## 6) **What each plot tells you**

### **Heatmap (imshow)**

- Rows = channels  
- Columns = time  
- Colour = firing rate  
- Shows structure, noise, outliers  

### **Average PSTH**

- Shows condition differences  
- Helps identify meaningful time windows  

### **PCA trajectory**

- Shows population‑level dynamics  
- Reveals separation between conditions  
- Shows loops, attractors, transitions  

---

## 7) **Common mistakes (and how to avoid them)**

- ❌ Using parentheses on dicts  
  ✔️ Use `matdat['key']`

- ❌ Forgetting to flatten time vectors  
  ✔️ Use `TIME = matdat['t'][0]`

- ❌ Passing arrays into `extent`  
  ✔️ Use scalars only

- ❌ Feeding raw, noisy data into PCA  
  ✔️ Clean + normalise first

- ❌ Using wrong matrix orientation  
  ✔️ PCA expects `(samples, features)`  
     → `(timepoints, channels)`

- ❌ Mixing preferred and non‑preferred trials before PCA
  ✔️ Run PCA on each condition separately or concatenate with labels

---

## 8) **What PCA does NOT do**

- It does **not** find clusters  
- It does **not** find causality  
- It does **not** find “the neuron that matters”  
- It does **not** guarantee interpretability  
- PCA does **not** guarantee that PC1 corresponds to anything meaningful behaviourally
- PCA axes can flip sign arbitrarily

PCA axes can flip sign arbitrarily

It simply finds **the strongest patterns**.

---

## 9) **When PCA is the wrong tool**

Use something else if:

- dynamics are nonlinear → use t‑SNE, UMAP  
- you want rotational structure → use jPCA  
- you want latent dynamics → use GPFA  
- you want generative models → use LFADS  

But PCA is the perfect starting point.

---

## 10) **The one‑sentence summary**

> **PCA turns high‑dimensional neural activity into a small number of meaningful axes, letting you visualise how the brain’s population state evolves over time as a trajectory.**
