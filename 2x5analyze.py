f = open("2x5_counts.txt", "r")
lines = []
for i in f:
    j = i[1:-1].split(" ")
    j[-2] = j[-2][:-1]
    count = int(j[-1])
    lines.append((j[0:-1], count))

for i in lines:
    if i[1] == 0:
        print(i)
