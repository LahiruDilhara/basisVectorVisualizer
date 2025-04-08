import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Define 5 coordinates (closed shape)
points = [(1, 2), (4, 5), (6, 8), (9, 5), (5, 2)]

# Create a figure and axis
fig, ax = plt.subplots()

# Create a polygon patch (unfilled)
polygon = patches.Polygon(points, closed=True, edgecolor='blue', fill=False, linewidth=2)

# Add to the axis
ax.add_patch(polygon)

# Set limits
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Show plot
plt.show()