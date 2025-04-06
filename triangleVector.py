import numpy as np
import matplotlib.pyplot as plt

# Define three vectors (points)
v1 = np.array([3, 4])
v2 = np.array([-2, 1])
v3 = np.array([1, -3])

# Create figure and axis
fig, ax = plt.subplots()

# Plot coordinate axes
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)
ax.grid(True, linestyle="--", alpha=0.5)

# Plot vectors
ax.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='r', label="V1")
ax.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='g', label="V2")
ax.quiver(0, 0, v3[0], v3[1], angles='xy', scale_units='xy', scale=1, color='b', label="V3")

# Draw the triangle by connecting the three vectors
triangle = np.array([v1, v2, v3, v1])  # Closing the triangle
ax.plot(triangle[:, 0], triangle[:, 1], 'k-', linewidth=2, label="Triangle")

# Set limits
all_x = [v1[0], v2[0], v3[0]]
all_y = [v1[1], v2[1], v3[1]]
ax.set_xlim(min(all_x) - 1, max(all_x) + 1)
ax.set_ylim(min(all_y) - 1, max(all_y) + 1)

ax.legend()
plt.show()