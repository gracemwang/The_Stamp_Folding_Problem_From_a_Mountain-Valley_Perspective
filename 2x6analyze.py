bad5s = [[2,3,1,2], [2,3,1,4], [4,3,1,2], [4,3,1,4]]

def check5s(line):
    for i in bad5s:
        if (line[:-1] == i) or (line[1:] == i):
            return False
    return True


f = open("2x6_counts.txt", "r")
lines = []
for i in f:
    j = i[1:-1].split(" ")
    j[-2] = int(j[-2][:-1])
    for k in range(len(j) - 2):
        j[k] = int(j[k][:-1])
    count = int(j[-1])
    lines.append((j[0:-1], count))

for i in lines:
    if (i[1] == 0) and (check5s(i[0])):
        print(i)
