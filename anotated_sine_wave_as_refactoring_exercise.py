"""3D Sine-Wave example for a refactoring exercise.

Run with Python to display the original and refactored 3D sine waves.
"""
# See readme file for how to import numpy from terminal 

import matplotlib.pyplot as plt
import numpy as np


def unrefactored_wave(ax):
    """Plot the original version of the radial sine wave."""
    x_values = np.linspace(-10, 10, 160) # Describes what the x axis should look like/contain
    y_values = np.linspace(-10, 10, 160)# Describes what the y axis should look like/contain
    x_grid, y_grid = np.meshgrid(x_values, y_values) # Turns two 1D coordinate arrays into full 2D grids for plot simulation/math modelling
    heights = np.sin(np.sqrt(x_grid * x_grid + y_grid * y_grid)) # Computes a radial sine wave over a 2D grid (ripple)

# Turns 3D plot into a surface by sending computed grid of coordinates to matplotlib's 3D engines which render a shaded, coloured, 
# mesh-based surface.

    surface = ax.plot_surface(
        x_grid, y_grid, heights, cmap="viridis", linewidth=0
    )
    ax.set_title("Before: unrefactored")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("sin(sqrt(x^2 + y^2))")
    ax.view_init(elev=28, azim=55)

    return surface

# Constructor for sine wave model class:
# Container for user-given values to be stored within this instance for the rest of the class to use.

class SineWaveModel:
    """Generate reusable coordinates and heights for a radial sine wave."""

# A construcdtor is a method in a class that runs automatically when an object is created. In python it is always named __init__ 
# it receives the settings the user specifies, stores them (in the related object) and prepares the object to be used. 

    def __init__(self, extent=10, resolution=160, frequency=1.0): # This line defines the construcdtor class
        self.extent = extent # this parameter says how wide our constructor grid is
        self.resolution = resolution # decides how many points the model uses in the wave's x-y grid. Controls how smith/blocky it looks.
        self.frequency = frequency

# The following method is the part of the class controlling the 2D coordinate grid the wave is built on.  
# Turns model settings (extent vs resolution) into actual xy values for plotting / computation.

    def coordinates(self):
        values = np.linspace(-self.extent, self.extent, self.resolution)
        return np.meshgrid(values, values)

# Determines wave heights. Computes the sine of the distance from the origin, making the riple pattern in the plot.
    def heights(self, x, y):
        radius = np.hypot(x, y)
        return np.sin(self.frequency * radius)

# Takes a mathematical model (SineWaveModel) and turnsinto raw data required to draw 3D surface.
def plot_wave(ax, model, title):
    """Render any sine-wave model with consistent presentation."""
    x, y = model.coordinates()
    z = model.heights(x, y)

    ax.plot_surface(
        x, y, z, cmap="viridis", linewidth=0, antialiased=True
    )
    ax.set(title=title, xlabel="x", ylabel="y", zlabel="height")
    ax.view_init(elev=28, azim=55)

# The main() function is the orchestration layer of the plot program. It sets up figures, 
# makes subplots, calls wave-rendering functions and displays results.
# Suptitle instead of subtitle .: matplotlib does not have a subtitle function. title-> individual subplot
# subtitle -> for the entire figure. 
# figure.suptitle(...) adds a title above the whole figure centered across all subplots
# ax.set_title(...) adds a title inside a specific subplot
# subtitle(...)  Does not exist but can be faked using fig.text()

def main():
    figure = plt.figure(figsize=(14, 6))
    before = figure.add_subplot(1, 2, 1, projection="3d")
    after = figure.add_subplot(1, 2, 2, projection="3d")

    unrefactored_wave(before)
    plot_wave(after, SineWaveModel(), "After: refactored")

    figure.suptitle("3D Sine Wave Refactoring", fontsize=16)
    figure.tight_layout()
    plt.show()

# Control for when script runs its main logic. Every Python fiel has a built-in variable called __name__
# Python sets it automatically depending on how the file is being used.
# Most programs need to be run when they're executed directly and not when they're imported.
# You need the facility to reuse functions without launching plots 
# You need a way to separate script behaviour from model behaviour.
if __name__ == "__main__":
    main()

# NEXT STEPS
# This script is only designed to present a static 3D plot. 
# To step things up, use matplotlib.animation.FuncAnimation to use a function that updates
# the wave over time. Would also need a writer to save the animation (eg. FFmpeg).
# Could therefore build a rotating 3D wave animation, rippling wave animation, video file
# Interactive animation.