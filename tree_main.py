from helper_functions import create_permutations,von_neumann_neighbours,moore_neighbours
import numpy as np

def tree(i, j, new_array, treeN,t_n,N,r):
  p = 1/8
  arr = np.copy(new_array)
  not_treeN = create_permutations(t_n,treeN)
  
  global neighbours

  if (arr[i,j] == t_n and i>0 and j>0 and i<N-r-1 and j < N-r-1):
    
    if p > np.random.uniform(0,1):
      if arr[i - 1][j] ==0:
        neighbours = moore_neighbours(arr,i-1,j)
        von_neighbours = von_neumann_neighbours(i-1,j,r)
        if all(arr[tuple(m)] != k for m in von_neighbours for k in not_treeN) and sum(neighbours)<=2*t_n:
          arr[i - 1][j] = t_n

    elif p > np.random.uniform(0,1):
      if arr[i][j - 1] == 0:
        neighbours = moore_neighbours(arr,i,j-1)
        von_neighbours = von_neumann_neighbours(i,j-1,r)
        if all(arr[tuple(m)] != k for m in von_neighbours for k in not_treeN)and sum(neighbours)<=2*t_n:
          arr[i][j - 1] = t_n

    elif p > np.random.uniform(0,1):
      if arr[i - 1][j - 1] ==0:
        neighbbours = moore_neighbours(arr,i-1,j-1)
        von_neighbours = von_neumann_neighbours(i-1,j-1,r)
        if all(arr[tuple(m)] != k for m in von_neighbours for k in not_treeN)and sum(neighbours)<=2*t_n:
          arr[i - 1][j - 1] = t_n

    elif p > np.random.uniform(0,1):
      if arr[i + 1][j] == 0:
        neighbours = moore_neighbours(arr,i+1,j)
        von_neighbours = von_neumann_neighbours(i+1,j,r)
        if all(arr[tuple(m)] != k for m in von_neighbours for k in not_treeN)and sum(neighbours)<=2*t_n:
          arr[i + 1][j] = t_n


    elif p > np.random.uniform(0,1):
      if arr[i][j + 1] == 0:
        neighbours = moore_neighbours(arr,i,j+1)
        von_neighbours = von_neumann_neighbours(i,j+1,r)
        if all(arr[tuple(m)] != k for m in von_neighbours for k in not_treeN)and sum(neighbours)<=2*t_n:
          arr[i][j + 1] =t_n

    elif p > np.random.uniform(0,1):
      if arr[i + 1][j + 1] == 0:
        neighbours = moore_neighbours(arr,i+1,j+1)
        von_neighbours = von_neumann_neighbours(i+1,j+1,r)
        if all(arr[tuple(m)] != k for m in von_neighbours for k in not_treeN)and sum(neighbours)<=2*t_n:
          arr[i + 1][j + 1] = t_n

    elif p > np.random.uniform(0,1):
      if arr[i + 1][j - 1] == 0:
        neighbours = moore_neighbours(arr,i+1,j-1)
        von_neighbours = von_neumann_neighbours(i+1,j-1,r)
        if all(arr[tuple(m)] != k for m in von_neighbours for k in not_treeN)and sum(neighbours)<=2*t_n:
          arr[i + 1][j - 1] = t_n

    elif p > np.random.uniform(0,1):
      if arr[i - 1][j + 1] ==0:
        neighbours = moore_neighbours(arr,i-1,j+1)
        von_neighbours = von_neumann_neighbours(i-1,j+1,r)
        if all(arr[tuple(m)] != k for m in von_neighbours for k in not_treeN)and sum(neighbours)<=2*t_n:
          arr[i - 1][j + 1] = t_n

    elif p > np.random.uniform(0,1):
      if arr[i - 1][j - 1] ==0:
        neighbours = moore_neighbours(arr,i-1,j-1)
        von_neighbours = von_neumann_neighbours(i-1,j-1,r)
        if all(arr[tuple(m)] != k for m in von_neighbours for k in not_treeN)and sum(neighbours)<=2*t_n:
          arr[i - 1][j - 1] = t_n
    
    
      
  return arr
