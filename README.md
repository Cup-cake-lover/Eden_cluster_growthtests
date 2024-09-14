# Excluding Eden Clusters


A cellular automaton eden cluster simulator -- A model to emulate crown shyness patterns

<img src="https://upload.wikimedia.org/wikipedia/commons/4/4b/Crown_shyness.jpg"/>


This python script works on the basis of growing Eden Clusters. A specific repulsion factor is added to produce repulsion

Usage:

type in command line :  `python3 run.py --r 2 --g 200 --t 100 --f filename.csv` (for example)    

`--r` flag : repulsion factor
`--g` flag : Grid size 
`--t` flag : final time till the simulation runs 
`--f` flag : filename containing seed indices

WARNING : Currently this code runs on the basis of the seed values put in the seeds.csv file. This file can be custom made where first colomn corresponds to x value\ of the index and next colomn corresponds to the y value of the index. Please add the seed point accordingly to your chose grid size.

# UPDATE : A new file for creation for random seed points are added 
Usage :  python3 random_seed_gen.py --g 200 --r 2 --s 6969 --N 5 \

`--r` flag : repulsion factor
`--g` flag : Grid size 
`--s` flag : Random seed value (Any integer) 
`--N` flag : Number of trees required. 

This can create any randomly distributed seed lattice.

Aknowledgements: Sandra Elsa Sanjai, University of Padua, Italy





