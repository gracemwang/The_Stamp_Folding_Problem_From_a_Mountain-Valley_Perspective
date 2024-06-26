"""
Analyze counts.txt and make a histogram of the counts.
"""

import matplotlib.pyplot as plt
import numpy as np

N = 22

strings = {}
numbers = {}
maxes = {}

for n in range(4, N+1):
    file_path = '1xn_data/1x{}counts.txt'.format(n)

    with open(file_path, 'r') as file:
        numbers[n] = []
        strings[n] = []
        for line in file:
            if ' ' in line:
                numbers[n].append(int(line.strip().split(' ')[1]))
                strings[n].append(line.strip().split(' ')[0])
            else:
                numbers[n].append(int(line.strip()))
        maxes[n] = max(numbers[n])

    # print(strings[n])
    # print(numbers[n])
    # print(maxes[n])

    # for i in range(len(numbers[n])):
    #     if numbers[n][i] == maxes[n]:
    #         print(strings[n][i], end=' ')
    # print()

for n in range(10, 23):
    plt.figure(figsize=(10, 6))
    plt.hist(numbers[n], bins= maxes[n], edgecolor='black')
    plt.xlabel('# of ways to fold')
    plt.ylabel("# of MV assignments that achieve X ways to fold")
    plt.title("The 1x{} case".format(n))
    plt.savefig('1xn_figures/1x{}_distribution.jpg'.format(n))
    # plt.show()