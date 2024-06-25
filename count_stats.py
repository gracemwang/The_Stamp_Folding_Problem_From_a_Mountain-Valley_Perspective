"""
Analyze counts.txt and make a histogram of the counts.
"""

import matplotlib.pyplot as plt

N = 21

def get_vals(n):
    file_path = '1xn_data/1x{}counts.txt'.format(n)

    with open(file_path, 'r') as file:
        numbers = [int(line.strip().split(' ')[-1]) for line in file]
        return numbers

maxes = {}
for n in range(4, N+1):
    maxes[n] = max(get_vals(n))
    if n > 4:
        print(maxes[n] / maxes[n-1])

print(maxes)

last_nums = get_vals(N)

counts = {}
for k in last_nums:
    if k not in counts:
        counts[k] = 0
    counts[k] += 1

# print(list(counts[i] if i in counts else 0 for i in range(1, maxes[N])))

#
# nums = maxes[1::2]
# for i in range(1, len(nums)):
#     print(nums[i] / nums[i-1])

plt.figure(figsize=(10, 6))
plt.hist(last_nums, bins=maxes[N], edgecolor='black')
plt.show()