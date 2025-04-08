import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation

# Define initial and final coordinates of the polygon
start_points = np.array([(1, 2), (4, 5), (6, 8), (9, 5), (5, 2)])
end_points = np.array([(2, 1), (5, 4), (7, 7), (8, 4), (4, 1)])

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Create a polygon patch (starting position)
polygon = patches.Polygon(start_points, closed=True, edgecolor='blue', facecolor='lightgreen', linewidth=2)
ax.add_patch(polygon)

# Function to update the animation
def update(frame):
    # Interpolate between start and end points
    new_points = (1 - frame) * start_points + frame * end_points
    polygon.set_xy(new_points)
    return polygon,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 1, 50), interval=50, blit=True)

# Show animation
plt.show()