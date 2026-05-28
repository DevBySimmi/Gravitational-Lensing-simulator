# 🌌 Gravitational Lensing Simulator

A Python-based gravitational lensing simulator that visualizes how massive objects bend light using Einstein’s general relativity concepts. Includes lens distortion, Einstein ring visualization, and space-time curvature effects.

---

## 🚀 Features

- 🧠 Physics-based light deflection model  
- 🌌 Visualization of space distortion  
- 🔵 Einstein ring representation  
- ⚡ Fast NumPy-based computation  
- 📊 2D grid-based lensing simulation  

---

## 📐 Physics Used

The simulation is based on the gravitational deflection formula:

\[
\alpha = \frac{4GM}{c^2 r}
\]

Where:
- G = gravitational constant  
- M = mass of lensing object  
- c = speed of light  
- r = distance from lens center  

Einstein radius is computed as:

\[
\theta_E = \sqrt{\frac{4GM}{c^2} \cdot \frac{D_{LS}}{D_L D_S}}
\]

---

## 🛠️ Requirements

```bash
numpy
matplotlib
