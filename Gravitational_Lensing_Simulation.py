# 🌌 ULTRA GRAVITATIONAL LENSING SIMULATION
# Features:
# ⭐ Background stars
# 🌀 Black hole accretion disk
# 🌈 Einstein Ring
# ⚡ Photon bending visualization
# 🎥 Animated spacetime lensing
# 🔥 Cinematic glow effects

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ==========================
# SIMULATION SETTINGS
# ==========================

GRID_SIZE = 120
SPACE_LIMIT = 2e21

BLACK_HOLE_MASS = 8e36
G = 6.67430e-11
c = 3e8

# Einstein radius
einstein_radius = 4e20

# ==========================
# CREATE SPACE GRID
# ==========================

x = np.linspace(-SPACE_LIMIT, SPACE_LIMIT, GRID_SIZE)
y = np.linspace(-SPACE_LIMIT, SPACE_LIMIT, GRID_SIZE)

X, Y = np.meshgrid(x, y)

# Distance from black hole
R = np.sqrt(X**2 + Y**2) + 1e18

# ==========================
# GRAVITATIONAL DEFLECTION
# ==========================

alpha = (4 * G * BLACK_HOLE_MASS) / (c**2 * R)

# Lensed coordinates
X_lens = X - alpha * (X / R) * 1e20
Y_lens = Y - alpha * (Y / R) * 1e20

# ==========================
# FIGURE
# ==========================

fig, ax = plt.subplots(figsize=(13, 8))
fig.patch.set_facecolor("black")
ax.set_facecolor("black")

# ==========================
# BACKGROUND STARS
# ==========================

np.random.seed(42)

stars_x = np.random.uniform(-SPACE_LIMIT, SPACE_LIMIT, 2000)
stars_y = np.random.uniform(-SPACE_LIMIT, SPACE_LIMIT, 2000)

ax.scatter(
    stars_x,
    stars_y,
    s=np.random.uniform(0.2, 2.5, 2000),
    color="white",
    alpha=0.8
)

# ==========================
# ACCRETION DISK
# ==========================

theta = np.linspace(0, 2*np.pi, 1000)

disk_r1 = 2.2e20
disk_r2 = 4.0e20

disk_x1 = disk_r1 * np.cos(theta)
disk_y1 = disk_r1 * np.sin(theta)

disk_x2 = disk_r2 * np.cos(theta)
disk_y2 = disk_r2 * np.sin(theta)

# Glow rings
for i in range(10):
    scale = 1 + i * 0.05
    ax.plot(
        disk_x1 * scale,
        disk_y1 * scale,
        color="orange",
        alpha=0.05,
        linewidth=8
    )

# Main disk
disk_line, = ax.plot(
    disk_x1,
    disk_y1,
    color="gold",
    linewidth=3
)

# ==========================
# EINSTEIN RING
# ==========================

ring_x = einstein_radius * np.cos(theta)
ring_y = einstein_radius * np.sin(theta)

einstein_ring, = ax.plot(
    ring_x,
    ring_y,
    color="cyan",
    linewidth=1.5,
    alpha=0.7
)

# ==========================
# BLACK HOLE CENTER
# ==========================

blackhole = plt.Circle(
    (0, 0),
    1.2e20,
    color="black",
    zorder=10
)

ax.add_patch(blackhole)

# Outer glow
for i in range(8):
    glow = plt.Circle(
        (0, 0),
        1.4e20 + i*0.3e20,
        color="purple",
        alpha=0.03
    )
    ax.add_patch(glow)

# ==========================
# LENSED PHOTONS
# ==========================

photons = ax.scatter(
    X_lens,
    Y_lens,
    s=1,
    color="deepskyblue",
    alpha=0.45
)

# ==========================
# MOVING SOURCE STAR
# ==========================

source, = ax.plot(
    [],
    [],
    'o',
    color='red',
    markersize=10
)

# ==========================
# TITLE & LABELS
# ==========================

ax.set_title(
    "Cinematic Gravitational Lensing Simulation",
    color="white",
    fontsize=18
)

ax.set_xlabel("X Position (m)", color="white")
ax.set_ylabel("Y Position (m)", color="white")

ax.tick_params(colors='white')

# ==========================
# LIMITS
# ==========================

ax.set_xlim(-SPACE_LIMIT, SPACE_LIMIT)
ax.set_ylim(-SPACE_LIMIT, SPACE_LIMIT)

# ==========================
# ANIMATION
# ==========================

def animate(frame):

    # Rotate accretion disk
    angle = frame * 0.03

    rot_x = disk_r1 * np.cos(theta + angle)
    rot_y = disk_r1 * np.sin(theta + angle)

    disk_line.set_data(rot_x, rot_y)

    # Pulsating Einstein ring
    pulse = 1 + 0.04 * np.sin(frame * 0.1)

    einstein_ring.set_data(
        ring_x * pulse,
        ring_y * pulse
    )

    # Moving source star
    sx = 6e20 * np.cos(frame * 0.02)
    sy = 6e20 * np.sin(frame * 0.02)

    source.set_data([sx], [sy])

    return disk_line, einstein_ring, source

# ==========================
# RUN ANIMATION
# ==========================

ani = FuncAnimation(
    fig,
    animate,
    frames=500,
    interval=30,
    blit=True
)

plt.tight_layout()
plt.show()