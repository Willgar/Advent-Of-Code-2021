"""
--- Day 13: Transparent Origami ---
You reach another volcanically active part of the cave. It would be nice if you could do some kind of thermal imaging so you could tell ahead of time which caves are too hot to safely enter.

Fortunately, the submarine seems to be equipped with a thermal camera! When you activate it, you are greeted with:

Congratulations on your purchase! To activate this infrared thermal imaging
camera system, please enter the code found on page 1 of the manual.
Apparently, the Elves have never used this feature. To your surprise, you manage to find the manual; as you go to open it, page 1 falls out. It's a large sheet of transparent paper! The transparent paper is marked with random dots and includes instructions on how to fold it up (your puzzle input). For example:

6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
The first section is a list of dots on the transparent paper. 0,0 represents the top-left coordinate. The first value, x, increases to the right. The second value, y, increases downward. So, the coordinate 3,0 is to the right of 0,0, and the coordinate 0,7 is below 0,0. The coordinates in this example form the following pattern, where # is a dot on the paper and . is an empty, unmarked position:

...#..#..#.
....#......
...........
#..........
...#....#.#
...........
...........
...........
...........
...........
.#....#.##.
....#......
......#...#
#..........
#.#........
Then, there is a list of fold instructions. Each instruction indicates a line on the transparent paper and wants you to fold the paper up (for horizontal y=... lines) or left (for vertical x=... lines). In this example, the first fold instruction is fold along y=7, which designates the line formed by all of the positions where y is 7 (marked here with -):

...#..#..#.
....#......
...........
#..........
...#....#.#
...........
...........
-----------
...........
...........
.#....#.##.
....#......
......#...#
#..........
#.#........
Because this is a horizontal line, fold the bottom half up. Some of the dots might end up overlapping after the fold is complete, but dots will never appear exactly on a fold line. The result of doing this fold looks like this:

#.##..#..#.
#...#......
......#...#
#...#......
.#.#..#.###
...........
...........
Now, only 17 dots are visible.

Notice, for example, the two dots in the bottom left corner before the transparent paper is folded; after the fold is complete, those dots appear in the top left corner (at 0,0 and 0,1). Because the paper is transparent, the dot just below them in the result (at 0,3) remains visible, as it can be seen through the transparent paper.

Also notice that some dots can end up overlapping; in this case, the dots merge together and become a single dot.

The second fold instruction is fold along x=5, which indicates this line:

#.##.|#..#.
#...#|.....
.....|#...#
#...#|.....
.#.#.|#.###
.....|.....
.....|.....
Because this is a vertical line, fold left:

#####
#...#
#...#
#...#
#####
.....
.....
The instructions made a square!

The transparent paper is pretty big, so for now, focus on just completing the first fold. After the first fold in the example above, 17 dots are visible - dots that end up overlapping after the fold is completed count as a single dot.

How many dots are visible after completing just the first fold instruction on your transparent paper?


The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
Finish folding the transparent paper according to the instructions. The manual says the code is always eight capital letters.

What code do you use to activate the infrared thermal imaging camera system?
Note: text ended up a bit mushy with this implementation
"""

data = []
val = "input"
while 1:
    val = input()
    if val == "":
        break
    val = val.split(',')
    data.append(val)
    print(val)
folds = []
while 1:
    val = input()
    if val == "":
        break
    val = val.split(' ')
    val = val[2].split('=')
    folds.append(val)
    print(val)

largestx = 0
largesty = 0
for x in range(len(data)):
    if int(data[x][0]) > int(largestx):
        largestx = int(data[x][0])
    if int(data[x][1]) > int(largesty):
        largesty = int(data[x][1])
print(largestx, largesty, len(data))
tempdata = data[:]
grid = []
for x in range(largesty+1):
    #print("")
    grid.append([])
    for y in range(largestx+1):
        flag = 0
        for z in range(len(tempdata)):
            #print(tempdata[z][1],tempdata[z][0], x, y)
            if int(tempdata[z][1]) == x and int(tempdata[z][0]) == y:
                flag = 1
                break

        if flag == 1:
            grid[x].append("#")
            #print("#", end="")
        else:
            grid[x].append(".")
            #print(".", end="")

def fold_y(grid, y_fold):
    grid1 = grid[:y_fold]
    grid2 = grid[y_fold+1:]
    for i in range(len(grid1)):
        i2 = len(grid2)-i-1
        for j in range(len(grid1[i])):
            if grid2[i2][j] == "#":
                grid1[i][j] = "#"
    return grid1

def fold_x(grid, x_fold):
    grid1 = []
    grid2 = []
    for x in range(len(grid)):
        grid1.append(grid[x][:x_fold])
        #if(x_fold%2==1):
        grid2.append(grid[x][x_fold+1:])
        #else:
            #grid2.append(grid[x][x_fold:])

    for i in range(len(grid1)):
        for j in range(len(grid1[i])):
            j1 = len(grid2[x])-j-1
            if grid2[i][j1] == "#":
                grid1[i][j] = "#"
    return grid1

for fold in folds:
    if fold[0] == "y":
        grid = fold_y(grid, int(fold[1]))
    else:
        grid = fold_x(grid, int(fold[1]))
    index = 0
    for x in range(len(grid)):
        print("")
        for y in range(len(grid[x])):
            if(grid[x][y]=="#"):
                index+=1
            print(grid[x][y],end="")
    print("\n",index,"\n")
