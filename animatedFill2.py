import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

# Create a vector (initial state)
vector, = ax.plot([], [], 'ro-', lw=3, label="Vector")  # Red dot and line
fill = ax.fill_between([], [], color='blue', alpha=0.3)  # Initial fill (empty)

# Function to initialize the plot
def init():
    vector.set_data([], [])
    return vector, fill

# Function to update the plot for each frame
def update(frame):
    # Change vector direction dynamically
    theta = np.radians(frame)  # Convert frame number to angle
    x, y = np.cos(theta), np.sin(theta)
    
    # Update the vector line
    vector.set_data([0, x], [0, y])

    # Update fill under the curve (example fill)
    global fill
    fill.remove()  # Remove previous fill
    fill = ax.fill_between([0, x], [0, y], color='blue', alpha=0.3)  # New fill
    
    return vector, fill

# Create animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 360, 2), init_func=init, blit=False, interval=50)

plt.legend()
plt.show()