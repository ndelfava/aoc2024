import numpy as np

def is_increasing_6(lst):
    arr = np.array(lst)
    diff = np.diff(arr)
    return np.all(diff >= 1) and np.all(diff <= 3)

def is_decreasing_6(lst):
    arr = np.array(lst)
    diff = np.diff(arr)
    return np.all(diff <= -1) and np.all(diff >= -3)

def is_safe_with_dampener(values):
    # Original check
    if is_increasing_6(values) or is_decreasing_6(values):
        return True
    
    # Try removing each single level
    for i in range(len(values)):
        test_values = values[:i] + values[i+1:]
        if is_increasing_6(test_values) or is_decreasing_6(test_values):
            return True
    
    return False

f = open("input2.txt")
lines = f.readlines()
count = 0

for line in lines:
    values = list(map(int, line.split()))
    if is_safe_with_dampener(values):
        count += 1

print(count)