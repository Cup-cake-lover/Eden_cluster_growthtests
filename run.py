import argparse
from tree_main import tree
from helper_functions import HelperFunctions
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
import matplotlib

# Set plotting style
matplotlib.rcParams['figure.dpi'] = 200
plt.style.use('seaborn-v0_8-colorblind')

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--r', type=int, help="Repulsion factor", required=True)
parser.add_argument('--t', type=int, help="Run time", required=True)
parser.add_argument('--g', type=int, help="Grid size", required=True)
parser.add_argument('--f', type=str, help="Seed file name", required=True)

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

# Set up progress bar
pbar = tqdm(desc='Growing Trees Progress', total=t_0)

# Main simulation loop
while t < t_0:
    for i in range(N):
        for j in range(N):
            for t_n in range(1, treeN):
                new_arr = tree(i, j, new_arr, treeN, t_n, N, r, helper)
    t += 1
    pbar.update(1)

pbar.close()

# Create a binary array for visualization
binary_array = new_arr.copy()
binary_array[binary_array != 0] = 1

# Plotting the final result
plt.imshow(binary_array, cmap='Greens', origin='lower')
plt.scatter(scatter_seeds[:, 1], scatter_seeds[:, 0], marker='v', color='black', s=60)
plt.savefig('Shyness_picture.png')
plt.show()  # Optionally display the image immediately
