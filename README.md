# CrownshynessMaster
A cellular automaton crown shyness emulator

This python script works on the basis of growing Eden Clusters. A specific repulsion factor is added to produce repulsion

Usage:
type in command line :  python3 run.py --r 2 --g 200 --t 100 (for example)
--r flag : repulsion factor
--g flag : Grid size
--t flag : final time till the simulation runs

WARNING : Currently this code runs on the basis of the seed values put in the seeds.csv file. This file can be custom made where first colomn corresponds to x value of the index
and next colomn corresponds to the y value of the index. Please add the seed point accordingly to your chose grid size.

As of now the seed values correspond to a 200x200 grid, and of 9 trees, please change this accordingly based of usage.
