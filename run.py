import argparse
from tree_main import tree
from helper_functions import seed_parse
import matplotlib.pyplot as plt ; import numpy as np
import matplotlib
matplotlib.rcParams['figure.dpi']=200
plt.style.use('seaborn-v0_8-colorblind')

parser = argparse.ArgumentParser()
parser.add_argument('--r', type=int,help="Repulsion factor",required=True)
parser.add_argument('--t', type=int,help="Run time",required=True)
parser.add_argument('--g', type=int,help="Grid size",required=True)

args = parser.parse_args()  




N = args.g
sample_array = np.zeros((N,N))
new_arr,scatter_seeds = seed_parse(sample_array,'seeds.csv')
t = 0
t_0 = args.t
treeN = int(len(scatter_seeds)) + 1 
r = args.r
t_0 = args.t

while t<t_0:
  for i in range(N):
    for j in range(N):
      for t_n in range(1,treeN):
        new_arr = tree(i, j, new_arr, treeN,t_n,N,r)


  t += 1 ; print('Growing trees..,Time_elapsed=',t) 


#plt.imshow(new_arr,cmap='plasma',origin='lower')
binary_array = new_arr
for i in range(N):
  for j in range(N):
    if binary_array[i,j] != 0:
      binary_array[i,j] = 1

plt.imshow(binary_array,cmap='Greens')
plt.scatter(scatter_seeds[:,1],scatter_seeds[:,0],marker='v',color='black',s=60)
plt.savefig('Shyness_picture.png')



