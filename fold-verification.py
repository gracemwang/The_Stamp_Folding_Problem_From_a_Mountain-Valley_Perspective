'''
Given a 2xn grid with MV assignment and an ordering of faces, determine if this gives a valid map fold
'''

import itertools
import numpy as np

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
        if (assign[i] == 1):
            edge_assign[(top_left, top_left+2)] = -1*base
            edge_assign[(top_left+1, top_left+3)] = -1*base
            edge_assign[(top_left+2, top_left+3)] = -1*base
        if (assign[i] == 2):
            edge_assign[(top_left, top_left+2)] = base
            edge_assign[(top_left+1, top_left+3)] = -1*base
            edge_assign[(top_left+2, top_left+3)] = base
        if (assign[i] == 3):
            edge_assign[(top_left, top_left+2)] = base
            edge_assign[(top_left+1, top_left+3)] = base
            edge_assign[(top_left+2, top_left+3)] = -1*base
        if (assign[i] == 4):
            edge_assign[(top_left, top_left+2)] = -1*base
            edge_assign[(top_left+1, top_left+3)] = base
            edge_assign[(top_left+2, top_left+3)] = base
    return edge_assign

def verify(assignment, ordering):
    # check for crossing violations
    def check_crossings(edges):
        for e1, e2 in itertools.combinations(edges, 2):
            b1 = min(ordering[e1[0]], ordering[e1[1]])
            t1 = max(ordering[e1[0]], ordering[e1[1]])
            b2 = min(ordering[e2[0]], ordering[e2[1]])
            t2 = max(ordering[e2[0]], ordering[e2[1]])
            
            if b1 < b2 and t1 > b2 and t1 < t2 or b2 < b1 and t2 > b1 and t2 < t1:
                # print("CROSSING", e1, e2)
                return False
        return True
    
    bottom_edges = [(i, i+1) for i in range(0, 2 * n, 2)]
    left_edges = [(i, i+2) for i in range(0, 2 * n - 2, 4)] + [(i, i+2) for i in range(1, 2 * n - 2, 4)]
    right_edges = [(i, i+2) for i in range(1, 2 * n - 1, 4)] + [(i, i+2) for i in range(1, 2 * n - 2, 4)]
    # print(bottom_edges)
    # print(left_edges)
    # print(right_edges)
    
    if not check_crossings(bottom_edges) or not check_crossings(left_edges) or not check_crossings(right_edges):
        return False
    
    def adjacent_faces(face):
        adj = []
        if face - 2 >= 0:
            adj.append(face-2)
        if face + 2 < n:
            adj.append(face+2)
        if face % 2 == 0:
            adj.append(face+1)
        if face % 2 == 1:
            adj.append(face-1)
        return adj
    
    # Check that MV is respected: faces with +1 parity (same as the top left) need to be below faces that they share a valley fold with, but faces with -1 parity need to satisfy the opposite conditions
    def checkMV(faces, parity):
        for face in faces:
            for adj in adjacent_faces(face):
                edge = (min(adj, face), max(adj, face))
                # bunch of signs stuff lol
                if np.sign(ordering[face] - ordering[adj]) != parity * assignment[edge]:
                    # print("MV ERROR", face, adj)
                    return False
        return True
    
    positive_faces = list(range(0, 2*n, 4)) + list(range(3, 2*n, 4))
    negative_faces = list(range(2, 2*n, 4)) + list(range(1, 2*n, 4))
    
    if not checkMV(positive_faces, +1) or not checkMV(negative_faces, -1):
        return False
    
    return True

n = 5
assignment1 = convertToMV([2, 4, 2, 1])
# this is the inverse of the superposition, so ordering[face] = index in the superposition
# print(verify(assignment1, np.argsort([0, 1, 3, 2, 4, 5, 9, 7, 6, 8])))
# print(verify(assignment1, np.argsort([9, 0, 1, 3, 2, 4, 5, 7, 6, 8])))
# print(verify(assignment1, np.argsort([0, 1, 9, 3, 2, 4, 5, 7, 6, 8])))
# print(verify(assignment1, np.argsort([0, 1, 3, 2, 9, 4, 5, 7, 6, 8]))) this should not work? (2, 4) and (7, 9) cross?

for perm in itertools.permutations(range(2 * n)):
    if verify(assignment1, np.argsort(perm)):
        print(perm)