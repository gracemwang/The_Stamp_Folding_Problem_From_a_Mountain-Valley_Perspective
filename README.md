### The Stamp Folding Problem From a Mountain-Valley Perspective

This repository contains the files used to generate experimental data for The Stamp Folding research group at MathILy-EST 2024. The project's paper can be found [here](https://arxiv.org/abs/2503.23661).

`stamp_meander.c` is a modified version of code [written by Joe Sawada](https://www.socs.uoguelph.ca/~sawada/programs.html) that can count the valid layer orderings that respect an inputted mountain-valley assignment.

`experiment.py` is a wrapper around `stamp_meander.c` to allow for easy analysis and visualization of the results.

`data_figs/1xn_data` contains the raw counts for all assignments, as well other sequences.

`data_figs/1xn_figures` contains the histograms of the distribution of counts and figures from other experiments.
