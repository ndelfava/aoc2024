f = open("input3.txt")

lines = f.readlines()
total = 0
potentials = []
dnt = "don't()"
do = "do()"


for line in lines:
    for i in range(len(line)):
        if line[i:i+7] == dnt:
            while line[i:i+4] != do:
                continue
            continue
        elif line[i:i+4] == "mul(":
            j = i+4
            while line[j] != ")":
                j += 1
            if j-i < 12:
                potentials.append(line[i+4:j])

for p in potentials:
    if "," in p:
        if p.split(",")[0] == p.split(",")[0].strip() and p.split(",")[1] == p.split(",")[1].strip():
            total += int(p.split(",")[0].strip()) * int(p.split(",")[1].strip())

print(total)
