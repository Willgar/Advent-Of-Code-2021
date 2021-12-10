"""
--- Day 9: Smoke Basin ---
These caves seem to be lava tubes. Parts are even still volcanically active; small hydrothermal vents release smoke into the caves that slowly settles like rain.

If you can model how the smoke flows through the caves, you might be able to avoid it and be that much safer. The submarine generates a heightmap of the floor of the nearby caves for you (your puzzle input).

Smoke flows to the lowest point of the area it's in. For example, consider the following heightmap:

2199943210
3987894921
9856789892
8767896789
9899965678
Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a location can be.

Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)

In the above example, there are four low points, all highlighted: two are in the first row (a 1 and a 0), one is in the third row (a 5), and one is in the bottom row (also a 5). All other locations on the heightmap have some lower adjacent location, and so are not low points.

The risk level of a low point is 1 plus its height. In the above example, the risk levels of the low points are 2, 1, 6, and 6. The sum of the risk levels of all low points in the heightmap is therefore 15.

Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?


--- Part Two ---
Next, you need to find the largest basins so you know what areas are most important to avoid.

A basin is all locations that eventually flow downward to a single low point. Therefore, every low point has a basin, although some basins are very small. Locations of height 9 do not count as being in any basin, and all other locations will always be part of exactly one basin.

The size of a basin is the number of locations within the basin, including the low point. The example above has four basins.

The top-left basin, size 3:

2199943210
3987894921
9856789892
8767896789
9899965678
The top-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678
The middle basin, size 14:

2199943210
3987894921
9856789892
8767896789
9899965678
The bottom-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678
Find the three largest basins and multiply their sizes together. In the above example, this is 9 * 14 * 9 = 1134.

What do you get if you multiply together the sizes of the three largest basins?
"""
class Height:
    def __init__(self, x,y,value,checked=False):
        self.x = x
        self.y = y
        self.value = value
        self.checked=checked

roof = []
val = "in"
while val != "":
    val = input()
    if val=="":
        break

    roof.append(list(val))


tops = []
print(roof)
for x in range(len(roof)):
    for y in range(len(roof[x])):
        #print(x,y,roof[x][y], len(roof[x]), len(roof))
        if x == 0:
            if y == 0:
                if roof[x][y] < roof[x][y+1]  and roof[x][y] < roof[x+1][y]:
                    print("1",x,y,roof[x][y])
                    tops.append(Height(x,y,roof[x][y]))
            elif y == len(roof[x])-1:
                if roof[x][y] < roof[x][y-1]  and roof[x][y] < roof[x+1][y]:
                    print("2",x,y,roof[x][y])
                    tops.append(Height(x,y,roof[x][y]))
            else:
                if roof[x][y] < roof[x][y-1] and roof[x][y] < roof[x][y+1] and roof[x][y] < roof[x+1][y]:
                    print("3",x,y,roof[x][y])
                    tops.append(Height(x,y,roof[x][y]))
        elif x == len(roof)-1:
            #print("hello")
            if y == 0:
                if roof[x][y] < roof[x][y+1]  and roof[x][y] < roof[x-1][y]:
                    print("4",x,y,roof[x][y])
                    tops.append(Height(x,y,roof[x][y]))
            elif y == len(roof[x])-1:
                if roof[x][y] < roof[x][y-1]  and roof[x][y] < roof[x-1][y]:
                    print("5",x,y,roof[x][y])
                    tops.append(Height(x,y,roof[x][y]))
            else:
                if roof[x][y] < roof[x][y-1] and roof[x][y] < roof[x][y+1] and roof[x][y] < roof[x-1][y]:
                    print("6",x,y,roof[x][y])
                    tops.append(Height(x,y,roof[x][y]))
        elif y == len(roof[x])-1:
            if roof[x][y] < roof[x][y-1] and roof[x][y] < roof[x+1][y] and roof[x][y] < roof[x-1][y]:
                print("7",x,y,roof[x][y])
                tops.append(Height(x,y,roof[x][y]))
        elif y == 0:
            if roof[x][y] < roof[x][y+1] and roof[x][y] < roof[x+1][y] and roof[x][y] < roof[x-1][y]:
                print("7",x,y,roof[x][y])
                tops.append(Height(x,y,roof[x][y]))
        elif roof[x][y] < roof[x][y-1] and roof[x][y] < roof[x][y+1] and roof[x][y] < roof[x-1][y] and roof[x][y] < roof[x+1][y]:
            print("8",x,y,roof[x][y])
            tops.append(Height(x,y,roof[x][y]))

def try_neightbour(x,y):
    if (x<0) or (y<0):
        return 9
    try:
        return roof[x][y]
    except IndexError:
        return 9

def find_adj(x,y,adj):
    new_adj = []
    #print(adj)
    if int(try_neightbour(x+1,y)) < 9:
        #print("1",try_neightbour(x+1,y))
        if [x+1,y] not in adj:
            new_adj.append([x+1,y])
    if int(try_neightbour(x-1,y)) < 9:
        #print("2",try_neightbour(x-1,y))
        if [x-1,y] not in adj:
            new_adj.append([x-1,y])
    if int(try_neightbour(x,y+1)) < 9:
        #print("3",try_neightbour(x,y+1))
        if [x,y+1] not in adj:
            new_adj.append([x,y+1])
    if int(try_neightbour(x,y-1)) < 9:
        #print("4",try_neightbour(x,y-1))
        if [x,y-1] not in adj:
            new_adj.append([x,y-1])

    for x in range(len(new_adj)):
        #print(roof[new_adj[x][0]][new_adj[x][1]])
        if new_adj[x] not in adj:
            adj.append(new_adj[x])

    if new_adj == []:
        return adj
    else:
        #print(new_adj)
        for x in range(len(new_adj)):
            newstuff = find_adj(new_adj[x][0],new_adj[x][1], adj)
            for x in range(len(newstuff)):
                if newstuff[x] not in adj:
                    adj.append(newstuff[x])
    return adj


#newlist = find_adj(tops[0].x, tops[0].y, [[tops[0].x,tops[0].y]])
#print(tops)
sum = []
basin = []
for x in range(len(tops)):
    sum.append(find_adj(tops[x].x, tops[x].y, [[tops[x].x,tops[x].y]]))
    print(sum[len(sum)-1])
    basin.append(len(sum[len(sum)-1]))
basin.sort()
print(basin)
print(basin[len(basin)-1]*basin[len(basin)-2]*basin[len(basin)-3])
#print(sum)
#print(len(basin[len(basin)-1]),len(basin[len(basin)-2]),len(basin[len(basin)-3]))

#print(len(basin[len(basin)-1])*len(basin[len(basin)-2])*len(basin[len(basin)-3]))
