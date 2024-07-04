"""
Analyze counts.txt and make a histogram of the counts.
"""

import matplotlib.pyplot as plt
import numpy as np

N = 22

strings = {}
numbers = {}
maxes = {}

def get_assignment(index, n):
    return ("{0:0"+str(n)+"b}").format(index, n).replace('0', 'V').replace('1', 'M')

for n in range(4, N+1):
    file_path = 'data_figs/1xn_data/1x{}counts.txt'.format(n)

    with open(file_path, 'r') as file:
        numbers[n] = []
        strings[n] = []
        for i, line in enumerate(file):
            if ' ' in line:
                numbers[n].append(int(line.strip().split(' ')[1]))
                strings[n].append(line.strip().split(' ')[0])
            else:
                numbers[n].append(int(line.strip()))
                strings[n].append(get_assignment(i, n-1))
        maxes[n] = max(numbers[n])

    # print(strings[n])
    # print(numbers[n])
# print('\n'.join(str(maxes[n]) for n in range(4, N+1)))

    print(len(numbers[n]))
    print(n, end=' ')
    for i in range(len(numbers[n])):
        if numbers[n][i] == maxes[n]:
            print(strings[n][i], end=' ')
    print()

# for n in range(10, 23):
#     plt.figure(figsize=(10, 6))
#     plt.hist(numbers[n], bins=min(maxes[n], 100), edgecolor='black')
#     plt.xlabel('# of ways to fold')
#     plt.ylabel("# of MV assignments that achieve X ways to fold")
#     plt.title("The 1x{} case".format(n))
#     plt.savefig('1xn_figures/1x{}_distribution.jpg'.format(n))
#     # plt.show()