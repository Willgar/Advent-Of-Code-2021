
data = []
val = "input"
while 1:
    val = input()
    if val == "":
        break
    val = list(val)
    data.append(val)
    #print(val)
errors = []
for x in range(len(data)):
    comp = []
    for y in range(len(data[x])):
        if data[x][y] == '(' or data[x][y] == '[' or data[x][y] == '{' or data[x][y] == '<':
            comp.append(data[x][y])
        elif (comp[len(comp)-1]=="(" and data[x][y] == ')') or (comp[len(comp)-1]=="[" and data[x][y] == ']') or (comp[len(comp)-1]=="{" and data[x][y] == '}') or (comp[len(comp)-1]=="<" and data[x][y] == '>'):
            comp.pop()
        else:
            errors.append(data[x][y])
            print(data[x][y], comp[len(comp)-1])
            break
sum = 0
for x in range(len(errors)):
    if errors[x] == ')':
        sum += 3
    if errors[x] == ']':
        sum += 57
    if errors[x] == '}':
        sum += 1197
    if errors[x] == '>':
        sum += 25137

print(sum)
