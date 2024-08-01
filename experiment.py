"""
Helper functions to gather data and test conjectures on various MV assignments.

To use this, compile stamp_meander.c to an exec called stamp_meander:
gcc stamp_meander.c -o stamp_meander.

Runs the executable and pipes the output here for easier processing.
"""
import itertools
import random
import subprocess
import numpy as np
import math
import matplotlib.pyplot as plt

'''
Run all the assignments for 1xn.
Returns a list of counts in lexicographic order (V = 0, M = 1).
'''
def run_all(n):
    return list(map(int, subprocess.Popen(["./stamp_meander", "0", str(n)], stdout=subprocess.PIPE).communicate()[0].decode().split("\n")[:-1]))

'''
Run a particular assignment (string of M's and V's) and returns the count
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
Convert from an integer to a binary string of length n, with V = 0 and M = 1.
Example: get_assignment(12, 6) -> "VVMMVV"
'''
def get_assignment(index, n):
    return ("{0:0"+str(n)+"b}").format(index, n).replace('0', 'V').replace('1', 'M')

def first_diff(nums):
    return list(nums[i] - nums[i-1] for i in range(1, len(nums)))

def kthdiff(nums, k):
    if k == 1:
        return first_diff(nums)
    return first_diff(kthdiff(nums, k-1))

def get_random_assignment(n):
    s = ''
    for i in range(n):
        s += random.choice(['M', 'V'])
    return s

'''
Returns the sizes of each "block" of identical characters.
Ex: get_block_sizes("MMMVVMMMV") -> [3, 2, 3, 1]
'''
def get_block_sizes(s):
    sizes = []
    curr = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            curr += 1
        else:
            sizes.append(curr)
            curr = 1
    sizes.append(curr)
    return sizes

'''
Graphs product of block lengths vs num of ways each string folds
b = number of blocks, r = number of trials
[l, u) = range of values for each block length
'''
def run_random(b, r, l, u):
    x = []
    y = []

    for _ in range(r):
        s = ""
        prod = 1

        for i in range(b):
            k = random.randint(l, u)
            s += "M" * k if i % 2 == 0 else "V" * k
            prod *= k
        
        x.append(prod)
        y.append(run_one(s))

    plt.scatter(x, y)
    plt.show()


'''
Finds maximally foldable MV assignment of length N that satisfies:
- Only contains blocks of size 2 and 3
- Does not contain two consecutive blocks of size 3
'''
# N = 33, ran repeat=14 up to 1=270
# COMPUTE MAXES
def max_restricted(N):
    best_value = 0
    best_str = ""

    seq = list(nums for nums in itertools.product([2, 3], repeat=14) if sum(nums) == N-1)

    for iter, nums in enumerate(seq):
        print(iter, len(seq), best_value, best_str)

        good = True
        s = ""
        for i in range(len(nums)):
            if i % 2 == 0:
                s += 'M' * nums[i]
            else:
                s += 'V' * nums[i]
            if i > 1 and nums[i] == 3 and nums[i-1] == 3:
                good = False
        s += '-'

        if not good or len(s) != N:
            continue

        val = run_one(s)

        if best_value < val:
            best_value = val
            best_str = s

    print("COMPLETE")
    print(N, best_value, best_str)

'''
Checks all MV assignments of length n for the following condition:
c(a_1, a_2, ..., a_m) <= prod(index where M changes to V or vice versa)
'''
def ub_conj_1(n):
    for i in range(2 ** n):
        s = get_assignment(i, n)
        arr = get_block_sizes(s)
        prod = 1
        sum_a = 0
        for b in arr:
            sum_a += b
            prod *= sum_a
        
        if (run_one(s) > prod):
            print(s)
        
    print("Done!")

'''
Checks all MV assignments of length n for the following condition:
c(a_1, a_2, ..., a_m) <= (m^m/m!) x (a_1 x a_2 x ... x a_m)
'''
def ub_conj_2(n):
    for i in range(2 ** n):
        s = get_assignment(i, n)
        arr = get_block_sizes(s)
        m = len(arr)
        prod = 1
        for b in arr:
            prod *= b
        
        if (run_one(s) > (m ** m) / (math.factorial(m)) * prod):
            print(s)
        
    print("Done!")