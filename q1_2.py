myfile = open("input.txt")    

lines = myfile.readlines()

left = []
right = []

for x in lines:
    left.append(int(x.split()[0]))
    right.append(int(x.split()[1]))

left.sort()
right.sort()

total = 0

for i in range(len(left)):
    for j in range(len(right)):
        count = 0
        if right[j] == left[i]:
            count += 1
        total += left[i] * count
print(total)
