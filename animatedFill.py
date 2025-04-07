import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up figure
fig, ax = plt.subplots(figsize=(5, 5))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

# Initial vector
vector = ax.quiver(0, 0, 1, 0, angles='xy', scale_units='xy', scale=1, color='red')

# Initial filled polygon (triangle)
triangle = plt.Polygon([[0, 0], [1, 0], [0.5, 0.5]], color='blue', alpha=0.3)
ax.add_patch(triangle)

# Update function
def update(frame):
    angle = np.radians(frame)  # Convert frame to angle
    x, y = np.cos(angle), np.sin(angle)  # Compute new vector direction
    vector.set_UVC(x, y)  # Update vector
    
    # Change fill shape (update triangle)
    new_triangle = [[0, 0], [x, y], [0.5 * x, 0.5 * y]]
    triangle.set_xy(new_triangle)
    
    return vector, triangle

# Create animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 360, 2), interval=50)

plt.show()