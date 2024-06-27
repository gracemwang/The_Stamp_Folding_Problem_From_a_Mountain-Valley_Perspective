"""
To use this, compile stamp_meander.c to an exec called stamp_meander:
gcc stamp_meander.c -o stamp_meander.

Runs the executable and pipes the output here for easier processing.
"""
import random
import subprocess

import matplotlib.pyplot as plt

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
Run a particular assignment and get the valid permutations
'''
def get_perms(assignment):
    perms = list(subprocess.Popen(["./stamp_meander", "2", assignment], stdout=subprocess.PIPE).communicate()[0].decode().split("\n")[:-2])
    for i in range(len(perms)):
        perms[i] = list(map(int, perms[i].split(" ")[:-1]))
    return perms

'''
Convert from the index in an array of counts to the assignment at that index. Example: get_assignment(12, 6) -> "VVMMVV"
'''
def get_assignment(index, n):
    return ("{0:0"+str(n)+"b}").format(index, n).replace('0', 'V').replace('1', 'M')

def first_diff(nums):
    return list(nums[i] - nums[i-1] for i in range(1, len(nums)))

def kthdiff(nums, k):
    if k == 1:
        return first_diff(nums)
    return first_diff(kthdiff(nums, k-1))

# pattern experiments!
# nums = list(run_one('M' * k + 'V' * k) for k in range(1, 6))

def get_random_assignment(n):
    s = ''
    for i in range(n):
        s += random.choice(['M', 'V'])
    return s

for k in range(1, 15):
    print(run_one('M' + 'V' * k))
