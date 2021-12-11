"""
--- Part Two ---
It seems like the individual flashes aren't bright enough to navigate. However, you might have a better option: the flashes seem to be synchronizing!

In the example above, the first time all octopuses flash simultaneously is step 195:

After step 193:
5877777777
8877777777
7777777777
7777777777
7777777777
7777777777
7777777777
7777777777
7777777777
7777777777

After step 194:
6988888888
9988888888
8888888888
8888888888
8888888888
8888888888
8888888888
8888888888
8888888888
8888888888

After step 195:
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
If you can calculate the exact moments when the octopuses will all flash simultaneously, you should be able to navigate through the cavern. What is the first step during which all octopuses flash?
"""
class Dumbo:
    def __init__(self,level, flash=1):
        self.level = level
        self.flash = flash

dumbo = []
val = "in"
i = 0
while val != "":
    val = input()
    if val=="":
        break
    dumbo.append([])
    for x in range(len(list(val))):
        dumbo[i].append(Dumbo(int(list(val)[x]), 1))
    i+=1

def try_neightbour(x,y):
    if (x<0) or (y<0):
        return -1
    try:
        if dumbo[x][y].flash == 1:
            dumbo[x][y].level+=1
        else:
            return -1
    except IndexError:
        return -1

def flash(x,y, flashes):
    if dumbo[x][y].flash == 1:
        flashes+=1
        dumbo[x][y].level = 0
        dumbo[x][y].flash = 0
        try_neightbour(x+1,y-1)
        try_neightbour(x+1,y)
        try_neightbour(x+1,y+1)
        try_neightbour(x-1,y-1)
        try_neightbour(x-1,y)
        try_neightbour(x-1,y+1)
        try_neightbour(x,y+1)
        try_neightbour(x,y-1)
    return flashes

flashes = 0
for step in range(0,1000):
    for x in range(len(dumbo)):
        for y in range(len(dumbo[x])):
            dumbo[x][y].level += 1
    for t in range(0,100):
        for x in range(len(dumbo)):
            for y in range(len(dumbo[x])):
                if dumbo[x][y].level > 9:
                    flashes = flash(x,y, flashes)
    minimum = len(dumbo)*len(dumbo[0])
    counter = 0
    for x in range(len(dumbo)):
        for y in range(len(dumbo[x])):
            dumbo[x][y].flash = 1
            print(dumbo[x][y].level, end="")
            if dumbo[x][y].level == 0:
                counter+=1
        print("")
    print("\n")
    if minimum == counter:
        print("success",step+1)
        break

#print(flashes)
