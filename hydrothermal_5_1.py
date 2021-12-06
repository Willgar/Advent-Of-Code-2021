"""
--- Day 5: Hydrothermal Venture ---
You come across a field of hydrothermal vents on the ocean floor! These vents constantly produce large, opaque clouds, so it would be best to avoid them if possible.

They tend to form in lines; the submarine helpfully produces a list of nearby lines of vents (your puzzle input) for you to review. For example:

0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end the line segment and x2,y2 are the coordinates of the other end. These line segments include the points at both ends. In other words:

An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.

So, the horizontal and vertical lines from the above list would produce the following diagram:

.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....
In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the number of lines which cover that point or . if no line covers that point. The top-left pair of 1s, for example, comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.

To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.

Consider only horizontal and vertical lines. At how many points do at least two lines overlap?


--- Part Two ---
Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need to also consider diagonal lines.

Because of the limits of the hydrothermal vent mapping system, the lines in your list will only ever be horizontal, vertical, or a diagonal line at exactly 45 degrees. In other words:

An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.
Considering all lines from the above example would now produce the following diagram:

1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111....
You still need to determine the number of points where at least two lines overlap. In the above example, this is still anywhere in the diagram with a 2 or larger - now a total of 12 points.

Consider all of the lines. At how many points do at least two lines overlap?
"""
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
