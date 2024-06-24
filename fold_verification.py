"""
Given a 2xn grid with MV assignment and an ordering of faces, determine if this gives a valid map fold
"""

import itertools
import numpy as np

n = 4

adj = {}
for face in range(2 * n):
    adj[face] = []
    if face - 2 >= 0:
        adj[face].append(face-2)
    if face + 2 < n:
        adj[face].append(face+2)
    if face % 2 == 0:
        adj[face].append(face+1)
    if face % 2 == 1:
        adj[face].append(face-1)

bottom_edges = [(i, i+1) for i in range(0, 2 * n, 2)]
left_edges = [(i, i+2) for i in range(0, 2 * n - 2, 4)] + [(i, i+2) for i in range(1, 2 * n - 2, 4)]
right_edges = [(i, i+2) for i in range(2, 2 * n - 2, 4)] + [(i, i+2) for i in range(3, 2 * n - 2, 4)]
# print(bottom_edges)
# print(left_edges)
# print(right_edges)

positive_faces = list(range(0, 2*n, 4)) + list(range(3, 2*n, 4))
negative_faces = list(range(2, 2*n, 4)) + list(range(1, 2*n, 4))

# check for crossing violations
def check_crossings(edges, ordering):
    for e1, e2 in itertools.combinations(edges, 2):
        b1 = min(ordering[e1[0]], ordering[e1[1]])
        t1 = max(ordering[e1[0]], ordering[e1[1]])
        b2 = min(ordering[e2[0]], ordering[e2[1]])
        t2 = max(ordering[e2[0]], ordering[e2[1]])

        if b1 < b2 < t1 < t2 or b2 < b1 < t2 < t1:
            # print("CROSSING", e1, e2, b1, t1, b2, t2)
            return False
    return True

    # points = []
    # for edge in edges:
    #     b = min(ordering[edge[0]], ordering[edge[1]])
    #     t = max(ordering[edge[0]], ordering[edge[1]])
    #     points.append((b, 'b'))
    #     points.append((t, 't'))
    #
    # points.sort(key=lambda e: e[0])
    #
    # i = 0
    # while i < len(points):
    #     while points[i][1] == 'b':
    #         i += 1
    #         if i == len(points):
    #             return False
    #     if points[i-1][0] != points[i][0]:
    #         return False
    #
    #     del points[i-1]
    #     del points[i-1]
    #     i -= 1
    #
    # return len(points) == 0

# Check that MV is respected: faces with +1 parity (same as the top left) need to be below faces that they share a
# valley fold with, but faces with -1 parity need to satisfy the opposite conditions
def checkMV(faces, parity, assignment, ordering):
    for face in faces:
        for adj_ in adj[face]:
            edge = (min(adj_, face), max(adj_, face))
            # bunch of signs stuff lol
            if np.sign(ordering[face] - ordering[adj_]) != parity * assignment[edge]:
                # print("MV ERROR", face, adj)
                return False
    return True

def verify(assignment, ordering):
    if not checkMV(positive_faces, +1, assignment, ordering) or not checkMV(negative_faces, -1, assignment, ordering):
        return False

    if not check_crossings(bottom_edges, ordering) or not check_crossings(left_edges, ordering) or not check_crossings(right_edges, ordering):
        return False

    return True

'''
Input: n-1 length list with entries {1, 2, 3, 4} for each internal vertex. The number is the unique edge around that vertex, with 1: left, 2: bottom, 3: right, 4: top
Output: dictionary of MV edge assignments
'''
def convertToMV(assign):
    edge_assign = {}
    edge_assign[(0,1)] = -1
    for i in range(len(assign)):
        top_left = 2*i
        base = edge_assign[(top_left, top_left+1)]
        if assign[i] == 1:
            edge_assign[(top_left, top_left+2)] = -1*base
            edge_assign[(top_left+1, top_left+3)] = -1*base
            edge_assign[(top_left+2, top_left+3)] = -1*base
        if assign[i] == 2:
            edge_assign[(top_left, top_left+2)] = base
            edge_assign[(top_left+1, top_left+3)] = -1*base
            edge_assign[(top_left+2, top_left+3)] = base
        if assign[i] == 3:
            edge_assign[(top_left, top_left+2)] = base
            edge_assign[(top_left+1, top_left+3)] = base
            edge_assign[(top_left+2, top_left+3)] = -1*base
        if assign[i] == 4:
            edge_assign[(top_left, top_left+2)] = -1*base
            edge_assign[(top_left+1, top_left+3)] = base
            edge_assign[(top_left+2, top_left+3)] = base
    return edge_assign

for compressed_assignment in list(itertools.product([1, 2, 3, 4], repeat=4)):
    count = 0
    for perm in itertools.permutations(range(2 * n)):
        count += verify(convertToMV(compressed_assignment), np.argsort(perm))
    print(compressed_assignment, count)