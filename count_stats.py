import matplotlib.pyplot as plt

# Read numbers from a file
file_path = 'counts.txt'

with open(file_path, 'r') as file:
    numbers = [int(line.strip().split(' ')[-1]) for line in file]
    
print(numbers)

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.hist(numbers, bins=10, edgecolor='black')
plt.show()