import numpy as np
import matplotlib.pyplot as plt

# Define three vectors
v1 = np.array([3, 4])
v2 = np.array([-2, 1])
v3 = np.array([1, -3])
origin = np.array([0, 0])

# Create figure and axis
fig, ax = plt.subplots()

# Plot coordinate axes
ax.axhline(0, color='black', linewidth=1)  # X-axis
ax.axvline(0, color='black', linewidth=1)  # Y-axis
ax.grid(True, linestyle="--", alpha=0.5)

# Plot the vectors
ax.quiver(origin[0], origin[1], v1[0], v1[1], angles='xy',
          scale_units='xy', scale=1, color='r', label="V1")
ax.quiver(origin[0], origin[1], v2[0], v2[1], angles='xy',
          scale_units='xy', scale=1, color='g', label="V2")
ax.quiver(origin[0], origin[1], v3[0], v3[1], angles='xy',
          scale_units='xy', scale=1, color='b', label="V3")

# Set plot limits
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

# Add legend
ax.legend()

# Show the plot
plt.show()
