"""
Analyze counts.txt and make a histogram of the counts.
"""

import matplotlib.pyplot as plt

N = 10

strings = {}
numbers = {}
maxes = {}

for n in range(4, 21):
    file_path = '1xn_data/1x{}counts.txt'.format(n)

    with open(file_path, 'r') as file:
        numbers[n] = []
        strings[n] = []
        for line in file:
            numbers[n].append(int(line.strip().split(' ')[1]))
            strings[n].append(line.strip().split(' ')[0])
        maxes[n] = max(numbers[n])

    # print(strings[n])
    # print(numbers[n])
    # print(maxes[n])

    # print(numbers[6][3] == maxes[6])
    # print(strings[6][3])

    for i in range(len(numbers[n])):
        if numbers[n][i] == maxes[n]:
            print(strings[n][i], end=' ')
    print()

# plt.figure(figsize=(10, 6))
# plt.hist(numbers[N], bins=maxes[N], edgecolor='black')
# plt.xlabel('# of ways to fold')
# plt.ylabel("# of MV assignments that achieve X ways to fold")
# plt.title("The 1x21 case")
# plt.show()