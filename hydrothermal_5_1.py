
x1 = []
y1 = []
x2 = []
y2 = []

val = "start"
#data.append(val)
while val != "":
    val = input()
    if val=="":
        break
    val = val.split()
    first = val[0].split(',')
    second = val[2].split(',')
    x1.append(int(first[0]))
    y1.append(int(first[1]))
    x2.append(int(second[0]))
    y2.append(int(second[1]))

grid = []
for x in range(0, 999):
    grid.append([])
    for y in range(0,999):
        grid[x].append(int(0))

print(len(x1))
for x in range(0,len(x1)):
    print(x1[x], y1[x],"->",x2[x],y2[x])
    if int(x1[x]) == int(x2[x]):
        if(y1[x] < y2[x]):
            for k in range(int(y1[x]), int(y2[x])+1):
                grid[int(x1[x])][k] += 1
        else:
            for k in range(int(y2[x]),int(y1[x])+1):
                grid[int(x1[x])][k] += 1
    if int(y1[x]) == int(y2[x]):
        if int(x1[x]) < int(x2[x]):
            for k in range(int(x1[x]), int(x2[x])+1):
                grid[k][int(y1[x])] += 1
        else:
            for k in range(int(x2[x]),int(x1[x])+1):
                grid[k][int(y1[x])] += 1
    if(abs(int(y1[x])-int(y2[x])) == abs(int(x1[x])-int(x2[x]))):
        if int(x1[x]) < int(x2[x]):
            stepsx = range(int(x1[x]),int(x2[x])+1)
        else:
            stepsx = range(int(x1[x]),int(x2[x])-1,-1)
        if int(y1[x]) < int(y2[x]):
            stepsy = range(int(y1[x]),int(y2[x])+1)
        else:
            stepsy = range(int(y1[x]),int(y2[x])-1, -1)
        for y in range(len(stepsy)):
            grid[stepsx[y]][stepsy[y]] += 1
cross = 0
for x in range(0, 999):
    for y in range(0,999):
        if grid[x][y] > 1:
            cross += 1
print(cross)
