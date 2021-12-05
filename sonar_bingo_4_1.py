
winning_numbers = []
val = input()
val=val.split(',')
for x in range(len(val)):
    winning_numbers.append(val[x])
input()
print(winning_numbers)

data = []
val = "input"
while val != "":
    block = []
    for i in range(0,5):
        val = input()
        if val =="":
            break
        val=val.split()
        block.append([val[0],val[1],val[2],val[3],val[4]])
    next=input()
    print("block: ",block)
    data.append(block)


def bingo(list, numbers):
    #print(numbers)
    win =[]
    for i in range(len(data)): #Each bingo board
        #print("data i", i,data[i])
        columns = [0,0,0,0,0]
        for j in range(len(data[i])):   #Each bingo row
            row = 0
            for x in range(len(data[i][j])):    #Each bingo column in row
                if data[i][j][x] in numbers:
                    row += 1
                    columns[x] += 1
                if row==5:
                    win.append(i)
                if columns[x]==5:
                    win.append(i)
    return win

numbers =[]
for k in range(len(winning_numbers)):
    numbers.append(winning_numbers[k])
    num = bingo(data, numbers)
    #print("BREAK HERE\n\n\n data",success)
    if(len(num) != 0):
        for success in num:
            win_sum = 0
            loss_sum = 0
            for i in range(len(data[success])):
                print(data[success][i])
                for j in range(len(data[success][i])):
                    if data[success][i][j] in numbers:
                        win_sum += int(data[success][i][j])
                    else:
                        #print(data[success][i][j])
                        loss_sum += int(data[success][i][j])

            #print(data[i])
            print(numbers[-1], "*", loss_sum, "=",int(numbers[-1])*loss_sum)
            break
numbers = []

def calculate(list, numbers):
    sum = 0
    print(numbers)
    for i in range(len(list)):
        print(list[i])
        for j in range(len(list[i])):
            if list[i][j] not in numbers:
                #print(int(list[i][j]))
                sum += int(list[i][j])
            #else:
                #print((list[i][j]), "is in numbers")
    print(numbers[-1], "*", sum, "=",int(numbers[-1])*sum)


def bingo2(numbers):
    #print(numbers)
    for i in range(len(data)): #Each bingo board
        #print(data[2])
        #print("data i", i,data[i])
        if data[i]!=-1:
            columns = [0,0,0,0,0]
            for j in range(len(data[i])):   #Each bingo row
                row = 0
                for x in range(len(data[i][j])):    #Each bingo column in row
                    if data[i]==-1:
                        break
                    if data[i][j][x] in numbers:
                        row += 1
                        columns[x] += 1
                    if row==5:
                        calculate(data[i], numbers)
                        data[i] = -1
                        print(data[i])
                        return i
                    if columns[x]==5:
                        calculate(data[i], numbers)
                        data[i] = -1
                        print(data[i])
                        return i
    return 0


for k in range(len(winning_numbers)):
    numbers.append(winning_numbers[k])
    x = bingo2(numbers)
    while x!=0:
        x = bingo2(numbers)
        print(data[x])
