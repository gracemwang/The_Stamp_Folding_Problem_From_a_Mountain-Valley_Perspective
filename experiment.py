"""
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

'''
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
Convert MV assignment to length of M and V blocks
'''
def block_convert(str):
    first = 0
    start = str[0]
    l = []
    i = 1
    while(i < len(str)):
        if str[i] != start:
            l.append(i - first)
            first = i
            start = str[i]
        i+=1
    l.append(len(str) - first)
    m = len(l)
    return (m**m)*math.prod(l)/math.factorial(m)

# PRODUCT VERSUS COUNT SCATTER
# x = []
# y = []
# rat = []

# b = 4
# for _ in range(100):
#     s = ""
#     p = 1
#     tot = 0
#     for i in range(b):
#         k = random.randint(5, 15)
#         tot += k
#         s += "M" * k if i % 2 == 0 else "V" * k
#         # p *= k
#     if (tot % b != 0):
#         adder = (b - (tot % b))
#         k += adder
#         tot += adder
#         s += "M" * adder if tot % 2 == 1 else "V" * adder
#     same = ""
#     for i in range(b):
#         same += "M" * (tot // b) if i % 2 == 0 else "V" * (tot // b)
#     fold1 = run_one(s)
#     fold2 = run_one(same)
#     x.append(fold1)
#     y.append(fold2)
#     if (fold2/fold1 < 1):
#         print("s: " + s)
#         print("same: " + same)
#     rat.append(fold2/fold1)
# plt.hist(rat)
# print(min(rat))
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


# appending more ms
# x = []
# y = []
# data = []

# b = 3
# adder = 30
# outs = []
# maxes = []

# for _ in range(100):
#     nums = []
#     diffs = []
#     s = ""
#     sameplace = 0
#     for i in range(b):
#         k = random.randint(5, 10)
#         s += "M" * k if i % 2 == 0 else "V" * k
#         if i % 2 == 0:
#             first = k
#         else:
#             second = k
#     nums.append(run_one(s))
#     for rounds in range(adder):
#         if b % 2 == 0:
#             s += "M"
#         else:
#             s += "V"
#         nums.append(run_one(s))
#     for i in range(len(nums) -1):
#         diffs.append(nums[i+1]-nums[i])
#     for i in range(len(diffs) - 1):
#         if (diffs[i+1] == diffs[i]):
#             sameplace = i
#             break
#         if (diffs[i+1] < diffs[i]):
#             maxplace = i
#             break
#     if sameplace == 0:
#         sameplace = len(diffs)
#     outs.append(sameplace - max(first, second))
#     maxes.append(maxplace)
#     # print(maxplace)
#     # print(diffs)
# # print(outs)
# print(max(outs))
# print(max(maxes))
# print(maxes)

#Conj: c(AB) >= c(A)c(B)
x = []
y = []

(a, b) = (5, 6)
cas = []
cbs = []
cabs = []
ratios = []

str_a = []
str_b = []

for _ in range(100):

    s_a = get_random_assignment(a)

    if (s_a[len(s_a)-1] == "M"):
        s_b = "V" + get_random_assignment(b - 1)
    else:
        s_b = "M" + get_random_assignment(b - 1)
    

    str_a.append(s_a)
    str_b.append(s_b)

    cas.append(run_one(s_a))
    cbs.append(run_one(s_b))

    joined = s_a + s_b
    cabs.append(run_one(joined))

for i in range(len(cas)):
    ratio = cabs[i] / cas[i] / cbs[i]
    if (ratio < 1):
        print("a: " + str_a[i])
        print("b: " + str_b[i])