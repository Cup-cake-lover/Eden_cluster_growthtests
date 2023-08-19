import numpy as np
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--r', type=int,help="Exclusion factor",required=True)
parser.add_argument('--N', type=int,help="Number_of_trees",required=True)
parser.add_argument('--g', type=int,help="Grid size",required=True)
parser.add_argument('--s', type=int,help="Seed Value (Any random int)",required=True)

args = parser.parse_args()  

N = args.g
treeN = args.N
r = args.r
seed_value = args.s

def random_seed_lattice(N,r,treeN,seed_value):
  random.seed(seed_value)
  xs = random.sample(range(0, int(N-r-1)), treeN)
  ys = random.sample(range(0, int(N-r-1)), treeN)
  seed_list = np.array(list(zip(xs,ys)))
  print("These will be your tree nodes",seed_list)
  np.savetxt("seeds.csv",seed_list.astype(int),delimiter=',')


random_seed_lattice(N,r,treeN,seed_value)
