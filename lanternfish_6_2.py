"""
--- Part Two ---
Suppose the lanternfish live forever and have unlimited food and space. Would they take over the entire ocean?

After 256 days in the example above, there would be a total of 26984457539 lanternfish!

How many lanternfish would there be after 256 days?
"""
fishes = []
val = input()
val = val.split(',')
print(val)
for time in range(9):
    #print(val[time])
    fishes.append(val.count(str(time)))
    start = val.count(time)
    #fishes[time].append(start)
    print(fishes[time])

for x in range(256):
    print(fishes[3])
    print("day",x+1)
    temp = fishes[0]
    fishes[0] = fishes[1]
    fishes[1] = fishes[2]
    fishes[2] = fishes[3]
    fishes[3] = fishes[4]
    fishes[4] = fishes[5]
    fishes[5] = fishes[6]
    fishes[6] = fishes[7]+temp
    fishes[7] = fishes[8]

    fishes[8] = temp
    print(fishes[0]+fishes[1]+fishes[2]+fishes[3]+fishes[4]+fishes[5]+fishes[6]+fishes[7]+fishes[8])
