import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

# Initial vector
vector, = ax.plot([], [], 'ro-', lw=3, label="Vector")  # Red dot and line
fill = ax.fill_between([], [], color='blue', alpha=0.3)  # Initial empty fill

# Start and end points for smooth transition
start_angle = 0   # Start at 0 degrees
end_angle = 90    # End at 90 degrees
frames = 50       # Total frames for smooth transition

# Function to initialize the plot
def init():
    vector.set_data([], [])
    return vector, fill

# Function to update the plot smoothly
def update(frame):
    # Interpolate angle (linear transition)
    theta = np.radians(start_angle + (end_angle - start_angle) * (frame / frames))
    
    # Compute new x, y values
    x, y = np.cos(theta), np.sin(theta)
    
    # Update vector position
    vector.set_data([0, x], [0, y])

    # Update fill area dynamically
    global fill
    fill.remove()  # Remove previous fill
    fill = ax.fill_between([0, x], [0, y], color='blue', alpha=0.3)  # New filled area
    
    return vector, fill

# Create animation (NO repeat)
ani = animation.FuncAnimation(fig, update, frames=frames, init_func=init, blit=False, interval=20, repeat=False)

plt.legend()
plt.show()
