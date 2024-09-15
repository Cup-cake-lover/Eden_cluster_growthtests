import argparse
from tree_main import tree
from helper_functions import HelperFunctions
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
import matplotlib
import matplotlib.animation as animation  # For animation

# Set plotting style
matplotlib.rcParams['figure.dpi'] = 200
plt.style.use('seaborn-v0_8-colorblind')

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--r', type=int, help="Repulsion factor", required=True)
parser.add_argument('--t', type=int, help="Run time", required=True)
parser.add_argument('--g', type=int, help="Grid size", required=True)
parser.add_argument('--f', type=str, help="Seed file name", required=True)
parser.add_argument('--animate', action='store_true', help="Enable animation of the growth")  # Add animation flag

args = parser.parse_args()

# Initialize variables
N = args.g
sample_array = np.zeros((N, N))
helper = HelperFunctions(grid_size=N, repulsion_factor=args.r)

# Parse seeds from the specified file (error handling for CSV)
try:
    new_arr, scatter_seeds = helper.seed_parse(sample_array, args.f)
except FileNotFoundError:
    print(f"Error: '{args.f}' file not found. Please provide the correct file.")
    exit()

# Set up the simulation parameters
t = 0
t_0 = args.t
treeN = int(len(scatter_seeds)) + 1
r = args.r

# Create a binary array for visualization
binary_array = new_arr.copy()
binary_array[binary_array != 0] = 1

# Set up progress bar
pbar = tqdm(desc='Growing Trees Progress', total=t_0)

# Prepare the figure for plotting or animation
fig, ax = plt.subplots()
img = ax.imshow(binary_array, cmap='Greens', origin='lower')
ax.scatter(scatter_seeds[:, 1], scatter_seeds[:, 0], marker='v', color='black', s=60)

def update_frame(frame):
    """Update the array for each frame in the animation."""
    global new_arr
    for i in range(N):
        for j in range(N):
            for t_n in range(1, treeN):
                new_arr = tree(i, j, new_arr, treeN, t_n, N, r, helper)
    binary_array = new_arr.copy()
    binary_array[binary_array != 0] = 1
    img.set_data(binary_array)
    pbar.update(1)
    return [img]

# If animation is enabled, generate and save the animation
if args.animate:
    ani = animation.FuncAnimation(fig, update_frame, frames=t_0, repeat=False, blit=True)

    # Save the animation as MP4
    writer = animation.FFMpegWriter(fps=30, metadata=dict(artist='Me'), bitrate=1800)
    ani.save("tree_growth.mp4", writer=writer)

    plt.show()  # Optionally display the animation after saving

else:
    # Main simulation loop without animation
    while t < t_0:
        for i in range(N):
            for j in range(N):
                for t_n in range(1, treeN):
                    new_arr = tree(i, j, new_arr, treeN, t_n, N, r, helper)
        t += 1
        pbar.update(1)

    pbar.close()

# Final visualization for both animation and non-animation cases
binary_array = new_arr.copy()
binary_array[binary_array != 0] = 1

# Plotting the final result
plt.imshow(binary_array, cmap='Greens', origin='lower')
plt.scatter(scatter_seeds[:, 1], scatter_seeds[:, 0], marker='v', color='black', s=60)
plt.savefig('Shyness_picture.png')  # Always save the final picture
plt.show()  # Optionally display the image immediately
