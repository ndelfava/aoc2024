f = open("input2.txt")

lines = f.readlines()
count = 0
buffer = 0


increasing = False
decreasing = False




for line in lines:
    values = line.split()
    for value in values:
        values[values.index(value)] = int(value)
    if values[0] > values[1]:
        for i in range(len(values)-1):
            if values[i] > values[i+1]:
                if (values[i] - values[i+1] >= 1) and (values[i] - values[i+1] <= 3):
                    decreasing = True
                else:
                    decreasing = False
                    break
            elif values[i-1] > values[i+1]:
                if values[i-1] - values[i+1] >= 1 and values[i-1] - values[i+1] <= 3:
                    buffer += 1
                    values.pop(i)
                    decreasing = True
            
                    
            #     else:
            #         decreasing = False
            #         break
            else:
                decreasing = False
                break
        if decreasing and buffer < 2:
            count += 1

    elif values[0] < values[1]:
        for j in range(len(values)-1):
            if values[j] < values[j+1]:
                if (values[j+1] - values[j] >= 1) and (values[j+1] - values[j] <= 3):
                    increasing = True
                else:
                    increasing = False
                    break
            elif values[j-1] < values[j+1]:
                if values[j+1] - values[j-1] >= 1 and values[j+1] - values[j-1] <= 3:
                    buffer += 1
                    values.pop(j)
                    increasing = True
                    
            #     # else:
            #     #     increasing = False
            #     #     break
            else:
                increasing = False
                break
        if increasing and buffer < 2:
            count += 1
print(count)
    



    

