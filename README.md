# Excluding Eden Clusters: A Cellular Automaton Simulator


This Python script simulates the growth of Eden clusters with the inclusion of a repulsion factor to emulate crown shyness patterns in tree canopies. The model is inspired by the phenomenon where tree crowns avoid touching, creating beautiful, intricate patterns in nature.


<img src="https://upload.wikimedia.org/wikipedia/commons/4/4b/Crown_shyness.jpg"/>

![Read more about crown shyness on Wikipedia](https://en.wikipedia.org/wiki/Crown_shyness)


## How it Works

The model is based on Eden Cluster growth, with an added repulsion factor that prevents clusters from growing too closely to one another. This introduces a behavior similar to crown shyness. The script grows clusters starting from seed points, and by adjusting parameters such as grid size, time, and repulsion factor, you can simulate different growth patterns.


### Features
-- Adjustable Repulsion: Control how strongly growing clusters repel each other with the `--r` flag.
-- Customizable Grid: Set the grid size for the simulation.
-- Seed File for Initial Cluster Points: Customize the starting points by providing a CSV file with seed indices.
-- Random Seed Generation: Automatically generate random seed points for the simulation.

### Requirements

-- Python 3.x
-- Numpy
-- Matplotlib

### Usage:

type in your favorite CLI;

```bash
python run.py --r 2 --g 200 --t 100 --f seeds.csv`
```

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
Image credits:
<a href="https://commons.wikimedia.org/wiki/File:Crown_shyness.jpg">Akasmita</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0">CC BY-SA 4.0</a>, via Wikimedia Commons




