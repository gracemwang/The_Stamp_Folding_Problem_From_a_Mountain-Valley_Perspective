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

def gen_poset(MV_assign):
    poset = []
    for edge in MV_assign:
        if (edge[0]%4 == 0 or edge[0]%4 == 3):
            if (MV_assign[edge] == -1):
                poset.append([edge[0], edge[1]])
            else:
                poset.append([edge[1], edge[0]])
        else:
            if (MV_assign[edge] == 1):
                poset.append([edge[0], edge[1]])
            else:
                poset.append([edge[1], edge[0]])
    return poset

print(gen_poset(convertToMV([1,3,1,4])))
