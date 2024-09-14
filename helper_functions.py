import numpy as np

class HelperFunctions:
    def __init__(self, grid_size, repulsion_factor):
        self.grid_size = grid_size
        self.repulsion_factor = repulsion_factor
  
    def seed_parse(self, sample_array, filename):
        seeds = np.loadtxt(filename, delimiter=',')
        scatter_seeds = []
        for i, j in enumerate(seeds):
            [ii, ij] = [int(j[0]), int(j[1])]
            sample_array[tuple([ii, ij])] = i + 1
            scatter_seeds.append(j)
        return sample_array, np.array(scatter_seeds)

    def create_permutations(self, t_n, treeN):
        not_treeN = list(range(1, treeN))
        not_treeN.remove(t_n)
        return not_treeN

    def von_neumann_neighbours(self, temp_i, temp_j):
        r = self.repulsion_factor
        f = lambda s, r: {s} | {(a + x, b + d - x) for d in (1, -1) * r for a, b in f(s, r - 1) for x in (0, d)}
        return list(f((temp_i, temp_j), r))

    def moore_neighbours(self, arr, temp_i, temp_j):
        neighbours = [
            arr[temp_i - 1, temp_j], arr[temp_i + 1, temp_j],
            arr[temp_i, temp_j - 1], arr[temp_i, temp_j + 1],
            arr[temp_i - 1, temp_j - 1], arr[temp_i + 1, temp_j + 1],
            arr[temp_i + 1, temp_j - 1], arr[temp_i - 1, temp_j + 1]
        ]
        return neighbours
