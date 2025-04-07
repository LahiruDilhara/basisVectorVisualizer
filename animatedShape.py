import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Initial vertices of the triangle
vertices = np.array([[2, 2], [3, 5], [4, 2]])
polygon = plt.Polygon(vertices, closed=True, color='blue', alpha=0.6)
ax.add_patch(polygon)

# Animation function
def update(frame):
    # Move the triangle to the right
    new_vertices = vertices + [frame * 0.1, 0]
    polygon.set_xy(new_vertices)
    return polygon,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=30, blit=False)

plt.show()