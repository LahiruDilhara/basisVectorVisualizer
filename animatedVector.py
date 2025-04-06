import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_xlabel("X-Axis")
ax.set_ylabel("Y-Axis")

# Define origin
origin = np.array([[0], [0]])

# Initial vector position
v_start = np.array([[0], [5]])  # Starts at (0,5)
v_end = np.array([[5], [0]])    # Moves to (5,0)

# Create quiver plot (vector)
quiver = ax.quiver(origin[0], origin[1], v_start[0], v_start[1], angles="xy", scale_units="xy", scale=1, color="r")

# Define animation update function
def update(frame):
    # Linear interpolation between start and end points
    t = frame / 100  # Normalized time (0 to 1)
    new_x = (1 - t) * v_start[0] + t * v_end[0]
    new_y = (1 - t) * v_start[1] + t * v_end[1]
    
    # Update vector position
    quiver.set_UVC(new_x, new_y)
    return quiver,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=20, blit=False)

# Show plot
plt.show()