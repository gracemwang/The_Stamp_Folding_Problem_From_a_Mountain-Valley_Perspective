"""
Starts from n=a to n=b-1 and reads prior data that stores all MV assignments with the number of ways each folds.
Prints the number of ways each assignment folds and the set of all maximally folding assignments for each n.
"""

a = 4
b = 18

for i in range(a, b):
    max = 0
    assignments = []
    f = open("data_figs/1xn_data/1x" + str(i) + "counts.txt")
    for line in f:
        count = int(line.split()[1])
        if (count> max):
            assignments = [line.split()[0]]
            max = count
        if (count == max):
            assignments.append(line.split()[0])
    print(str(i) + ": " + str(max))
    print(assignments)
