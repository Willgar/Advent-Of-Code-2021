
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
    errors.append([])
    comp = []
    flag = 0
    for y in range(len(data[x])):
        #print(comp)
        if data[x][y] == '(' or data[x][y] == '[' or data[x][y] == '{' or data[x][y] == '<':
            comp.append(data[x][y])
        elif (comp[len(comp)-1]=="(" and data[x][y] == ')') or (comp[len(comp)-1]=="[" and data[x][y] == ']') or (comp[len(comp)-1]=="{" and data[x][y] == '}') or (comp[len(comp)-1]=="<" and data[x][y] == '>'):
            comp.pop()
        else:
            flag = 1
            #errors.append(comp[len(comp)-1])
            #print(comp[len(comp)-1])
            #comp.pop()
            #for z in range(len(comp)):
#            print(comp[len(comp)-1])
#            if comp[len(comp)-1] == '(':
#                errors.append(')')
#            if comp[len(comp)-1] == '[':
#                errors.append(']')
#            if comp[len(comp)-1] == '{':
#                errors.append('}')
#            if comp[len(comp)-1] == '<':
#                errors.append('>')
#            print("")
#            flag = 1
            #break
#            print(data[x][y], comp[len(comp)-1])
            #break
    if flag == 0:
        print(x, comp)
        for z in range(len(comp)-1, -1, -1):
            #print(comp[z], z)
            if comp[z] == '(':
                errors[x].append(')')
            if comp[z] == '[':
                errors[x].append(']')
            if comp[z] == '{':
                errors[x].append('}')
            if comp[z] == '<':
                errors[x].append('>')


combined_sum = []
print(errors)
errors = [i for i in errors if i != []]
print(errors)

for x in range(len(errors)):
    sum = 0
    for y in range(len(errors[x])):
        sum = sum*5
        if errors[x][y] == ')':
            sum += 1
        if errors[x][y] == ']':
            sum += 2
        if errors[x][y] == '}':
            sum += 3
        if errors[x][y] == '>':
            sum += 4
    print(sum)
    combined_sum.append(sum)

combined_sum.sort()
print(combined_sum)
index = round(len(combined_sum)/2)
print(combined_sum[index], index, len(combined_sum))
