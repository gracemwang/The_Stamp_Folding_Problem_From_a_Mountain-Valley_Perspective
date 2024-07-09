"""
To use this, compile stamp_meander.c to an exec called stamp_meander:
gcc stamp_meander.c -o stamp_meander.

Runs the executable and pipes the output here for easier processing.
"""
import itertools
import random
import subprocess
import numpy as np

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

def get_random_assignment(n):
    s = ''
    for i in range(n):
        s += random.choice(['M', 'V'])
    return s

for k in [8]:
    print(run_one(("M" * k + "V" * k) * 4))

# PRODUCT VERSUS COUNT SCATTER
# x = []
# y = []
#
# b = 4
# for _ in range(100):
#     s = ""
#     p = 1
#     for i in range(b):
#         k = random.randint(8, 15)
#         s += "M" * k if i % 2 == 0 else "V" * k
#         p *= k
#     x.append(run_one(s))
#     y.append(p)
#
# plt.scatter(x, y)
# plt.show()

# COMPUTE MAXES
# best_value = 0
# best_str = ""

# N = 33 # N = 33, ran repeat=14 up to 1=270
# seq = list(nums for nums in itertools.product([2, 3], repeat=14) if sum(nums) == N-1)
#
# for iter, nums in enumerate(seq):
#     print(iter, len(seq), best_value, best_str)
#
#     good = True
#     s = ""
#     for i in range(len(nums)):
#         if i % 2 == 0:
#             s += 'M' * nums[i]
#         else:
#             s += 'V' * nums[i]
#         if i > 1 and nums[i] == 3 and nums[i-1] == 3:
#             good = False
#     s += '-'
#
#     if not good or len(s) != N:
#         continue
#
#     val = run_one(s)
#
#     if best_value < val:
#         best_value = val
#         best_str = s
#
# print("COMPLETE")
# print(N, best_value, best_str)