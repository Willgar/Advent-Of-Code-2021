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

#print(tops)
sum = 0
for x in range(len(tops)):
    print(tops[x].value)
    sum += int(tops[x].value)+1
print(sum)
