Software to experiment with 2 x n stamp maps. Each code file has a header describing its purpose. Newcomers should read `fold_verification.py` and `make_poset.py` first. `count_w_sage.ipynb` simply takes these two and their methods, and incorporates an important Sage function that can generate the linear extensions of a poset quickly. 

The data folder contains some results we have found useful to analyze. Files labeled `2x{n}_counts.txt` list the concise representation of an assignmen followed by the number of ways to fold it. The files with `foldable` in the name instead list `True` or `False` indicating the foldability.

Potential directions for future experimental efforts:
- implement the result in Nishat 2009 that would reduce the verification from quadratic to linear
- use optimization software and encode the constraints as an MILP or other program, which may or may not run faster
- continue to explore the substring exclusion idea (see `gen_bad.ipynb`) to speed things up

Fast generation of valid foldings of a 1 x n stamp map, adapting code by Sawada, in `stamp_meander.c`. Outputed data is in `1xn_data`
