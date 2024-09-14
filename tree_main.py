import numpy as np

def tree(i, j, new_array, treeN, t_n, N, r, helper):
    p = 1 / 8
    arr = np.copy(new_array)
    not_treeN = helper.create_permutations(t_n, treeN)

    # Define all possible neighbor positions
    neighbors_pos = [
        (i - 1, j),     # Up
        (i, j - 1),     # Left
        (i - 1, j - 1), # Up-Left
        (i + 1, j),     # Down
        (i, j + 1),     # Right
        (i + 1, j + 1), # Down-Right
        (i + 1, j - 1), # Down-Left
        (i - 1, j + 1)  # Up-Right
    ]

    # Check if the current position contains the tree and is within the bounds
    if arr[i, j] == t_n and i > 0 and j > 0 and i < N - r - 1 and j < N - r - 1:

        # Loop through all neighboring positions
        for ni, nj in neighbors_pos:
            if arr[ni, nj] == 0 and p > np.random.uniform(0, 1):
                # Get the Moore and Von Neumann neighbors for this position
                neighbours = helper.moore_neighbours(arr, ni, nj)
                von_neighbours = helper.von_neumann_neighbours(ni, nj)

                # Apply the same logic to decide if this tree can grow into the neighbor
                if all(arr[tuple(m)] != k for m in von_neighbours for k in not_treeN) and sum(neighbours) <= 2 * t_n:
                    arr[ni, nj] = t_n

    return arr
