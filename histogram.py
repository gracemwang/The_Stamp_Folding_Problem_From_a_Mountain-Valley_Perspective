"""
Create a histogram of the counts for all assignments on the 1xn strip.
"""

import matplotlib.pyplot as plt
import numpy as np
import random
from experiment import get_block_sizes

N = 20

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
                strings[n].append(line.strip().split(' ')[0])
                # numbers[n].append(int(line.strip().split(' ')[1]))
                numbers[n].append(np.prod(get_block_sizes(strings[n][-1])))
                numbers[-1] *= random.randint(1, )
            else:
                numbers[n].append(int(line.strip()))
                strings[n].append(get_assignment(i, n-1))
        maxes[n] = max(numbers[n])

plt.figure(figsize=(10, 6))
plt.hist(numbers[n], bins=min(maxes[n], 50), edgecolor='black')
plt.xlabel('# of ways to fold')
plt.ylabel("# of MV assignments that achieve X ways to fold")
plt.title("The 1x{} case".format(n))
# plt.savefig('1xn_figures/1x{}_distribution.jpg'.format(n))
plt.show()