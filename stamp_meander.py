"""
To use this, compile stamp_meander.c to an exec called stamp_meander:
gcc stamp_meander.c -o stamp_meander.

Runs the executable and pipes the output here for easier processing.
"""

import subprocess

'''
Run all the assignments for 1xn. Returns a list of counts in lexicographic order (V = 0, M = 1).
'''
def run_all(n):
    return list(map(int, subprocess.Popen(["./stamp_meander", "0", str(n)], stdout=subprocess.PIPE).communicate()[0].decode().split("\n")[:-1]))

'''
Run a particular assignment and returns the count
'''
def run_one(assignment):
    return int(subprocess.Popen(["./stamp_meander", "1", assignment], stdout=subprocess.PIPE).communicate()[0].decode())

'''
Convert from the index in an array of counts to the assignment at that index. Example: get_assignment(12, 6) -> "VVMMVV"
'''
def get_assignment(index, n):
    return ("{0:0"+str(n)+"b}").format(index, n).replace('0', 'V').replace('1', 'M')

print('MMVV' * 4)

for k in range(20):
    print(run_one('MMVV' * k))