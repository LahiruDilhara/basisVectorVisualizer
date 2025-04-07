import matplotlib.pyplot as plt

# Step 1: Define the 5 coordinates (you can modify these coordinates)
coordinates = [(2, 3), (4, 5), (6, 2), (5, 1), (3, 1)]

# Step 2: Separate the x and y coordinates
x, y = zip(*coordinates)

# Step 3: Plot the points
plt.scatter(x, y, color='red', label='Coordinates')

# Step 4: Connect the points to form a shape (polygon)
plt.plot(x + (x[0],), y + (y[0],), color='blue', label='Shape')

# Step 5: Fill the shape
plt.fill(x + (x[0],), y + (y[0],), color='lightblue', alpha=0.5, label='Filled Shape')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Polygon with 5 Coordinates')

# Show legend
plt.legend()

# Show the plot
plt.show()