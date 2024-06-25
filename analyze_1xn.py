for i in range(4, 18):
    max = 0
    assignments = []
    f = open("1xn_data/1x" + str(i) + "counts.txt")
    for line in f:
        count = int(line.split()[1])
        if (count> max):
            assignments = [line.split()[0]]
            max = count
        if (count == max):
            assignments.append(line.split()[0])
    print(str(i) + ": " + str(max))
    print(assignments)
