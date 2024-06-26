# Given a poset, creates a matrix representing the relationships between each pair of faces.
# [a, b] = 1 if a must be below b, -1 if a must be above b, and 0 if the relationship is unknown.

import make_poset
import math

def gen_array(poset):
    l = (len(poset) + 2) // 3 * 2
    zeros = [0] * l
    out = zeros * l
    for (left, right) in poset:
        out[(left*l) + right] = 1
        out[(right*l) + left] = -1
        for i in range(l):
            #checking what right is less than
            if out[(right*l) + i] == 1:
                out[(left*l) + i] = 1
                out[(i*l) + left] = -1
            #checking what left is greater than
            if out[(left*l) + i] == -1:
                out[(right*l) + i] = -1
                out[(i*l) + right] = 1
    return out

# def check_down(m):
#     l = math.floor(math.sqrt(len(m)))
#     num_edges = l // 2
#     for i in range(num_edges):
#         for j in range(i, num_edges):
#             if out[i*l + i+1] == 1 and out[j*l + j+1] == 1:
#                 #0 < 1 and 2 < 3
#             else if out[i*l + i+1] == 1 and out[j*l + j+1] == -1:
#                 #0 < 1 and 2 > 3
#             else if out[i*l + i+1] == -1 and out[j*l + j+1] == 1:
#                 #0 > 1 and 2 < 3
#             else if out[i*l + i+1] == -1 and out[j*l + j+1] == -1:
#                 #0 > 1 and 2 > 3
#             else:
#                 print("Shucks")
#                 exit()

def print_matrix(m):
    l = math.floor(math.sqrt(len(m)))
    for i in range(l):
        for j in range(l):
            if m[i*l + j] == -1:
                print(m[i*l + j], end=" ")
            else:
                print(m[i*l + j], end="  ")
        print("\n")

myPos = make_poset.gen_poset(make_poset.convertToMV([2,4,2,4]))
myMat = gen_array(myPos)
print_matrix(myMat)
