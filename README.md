# The Stamp Folding Problem From a Mountain-Valley Perspective

Software to find the number of ways to fold specified mountain-valley assignments on a 1 x n strip of stamps. 

## Files

`stamp_meander.c` contains the code to find all of the valid foldings . The algorithm is adapted from "Stamp Foldings, Semi-Meanders, and Open Meanders: Fast Generation Algorithms" by Joe Sawada and Roy Li. 

`experiment.py` is a wrapper program that calls `stamp_meander.c`, allowing for more streamlined exerimentation.

`data_figs` contains the number of ways to fold all mountain-valley assignments for strips up to length 22, the number of ways to fold mountain-valley assignments with equal length blocks, and figures visualizing this data as well as other experiments. 

Each file has a header giving more details. 
