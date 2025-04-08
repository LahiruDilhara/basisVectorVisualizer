import matplotlib.pyplot as plt
import numpy as np

def update_limits(event):
    """Adjust the axis limits dynamically when resizing the window."""
    width, height = fig.get_size_inches() * fig.dpi
    aspect_ratio = width / height
    
    grid_spacing = 1  # Define spacing between grid lines
    x_limit = 10 * aspect_ratio  # Scale x-axis based on aspect ratio
    y_limit = 10  # Keep y-axis limit fixed

    ax.set_xlim(-x_limit, x_limit)
    ax.set_ylim(-y_limit, y_limit)

    ax.set_xticks(np.arange(-x_limit, x_limit + grid_spacing, grid_spacing))
    ax.set_yticks(np.arange(-y_limit, y_limit + grid_spacing, grid_spacing))
    
    fig.canvas.draw()  # Redraw the figure

# Create the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect('equal')

# Initial setup
update_limits(None)

# Enable grid
ax.grid(True, linestyle='--', alpha=0.6)

# Connect resize event to update function
fig.canvas.mpl_connect('resize_event', update_limits)

plt.show()