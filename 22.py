def is_safe_report(values):
    # Check if the original report is safe
    if all(0 < values[i+1] - values[i] <= 3 for i in range(len(values)-1)):
        return True
    
    # Try removing each single level
    for i in range(len(values)):
        test_values = values[:i] + values[i+1:]
        if all(0 < test_values[j+1] - test_values[j] <= 3 for j in range(len(test_values)-1)):
            return True
    
    return False

# Read the input file
f = open("input2.txt")
lines = f.readlines()
count = 0

for line in lines:
    values = list(map(int, line.split()))
    if is_safe_report(values):
        count += 1

print(count)