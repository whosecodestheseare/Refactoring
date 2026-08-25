#!/usr/bin/env python
# coding: utf-8

# In[12]:


"""
3D Sine-Wave as example for Refactoring
Run with Python 3D Sine Wave
"""

import numpy as np
import matplotlib.pyplot as plt

# BEFORE duplicated calculations, unclear names, and plotting mixed with the model's data generation.

import numpy as np
import matplotlib.pyplot as plt

def unrefactored_wave(ax):
    a = np.linspace(-10, 10, 160)
    b = np.linspace(-10, 10, 160)
    aa, bb = np.meshgrid(a, b)
    cc = np.sin(np.sqrt(aa * aa + bb * bb))

    # FIX 1: cmap name corrected
    surface = ax.plot_surface(aa, bb, cc, cmap="viridis", linewidth=0)

    # FIX 2: spelling corrected
    ax.set_title("Before: unrefactored")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("sin(√(x² + y²))")

    # FIX 3: view_init arguments corrected
    ax.view_init(elev=28, azim=55)

    return surface


class SineWaveModel:
    """Generate reusable coordinates and heights for a radial sine wave."""

    def __init__(self, extent=10, resolution=160, frequency=1.0):
        self.extent = extent
        self.resolution = resolution
        self.frequency = frequency

    def coordinates(self):
        a = np.linspace(-self.extent, self.extent, self.resolution)
        b = np.linspace(-self.extent, self.extent, self.resolution)
        return np.meshgrid(a, b)

    def heights(self, x, y):
        radius = np.hypot(x, y)
        return np.sin(self.frequency * radius)


def plot_wave(ax, model, title):
    """Render any sine-wave model with consistent presentation."""
    x, y = model.coordinates()
    z = model.heights(x, y)

    # FIX 4: cmap name corrected
    ax.plot_surface(x, y, z, cmap="viridis", linewidth=0, antialiased=True)

    ax.set(title=title, xlabel="x", ylabel="y", zlabel="height")
    ax.view_init(elev=28, azim=55)


def main():
    figure = plt.figure(figsize=(14, 6))
    before = figure.add_subplot(1, 2, 1, projection="3d")
    after = figure.add_subplot(1, 2, 2, projection="3d")

    unrefactored_wave(before)
    plot_wave(after, SineWaveModel(), "After: refactored")

    figure.suptitle("3D Sine Wave Refactoring", fontsize=16)
    figure.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()



# In[ ]:




