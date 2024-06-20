from fold-verification import convertToMV,

def gen_poset(MV_assign):
    poset = []
    for edge in MV_assign:
        if (edge[0]%4 == 0 or edge[0]%4 == 3):
            if (MV_assign[edge] = -1):
                poset.append([edge[0], edge[1]])
            else:
                poset.append([edge[1], edge[0]])
        else:
            if (MV_assign[edge] = 1):
                poset.append([edge[0], edge[1]])
            else:
                poset.append([edge[1], edge[0]])
    return poset

print(gen_poset(convertToMV(2421)))
