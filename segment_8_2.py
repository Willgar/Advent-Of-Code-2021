"""
--- Part Two ---
Through a little deduction, you should now be able to determine the remaining digits. Consider again the first example above:

acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
cdfeb fcadb cdfeb cdbaf
After some careful analysis, the mapping between signal wires and segments only make sense in the following configuration:

 dddd
e    a
e    a
 ffff
g    b
g    b
 cccc
So, the unique signal patterns would correspond to the following digits:

acedgfb: 8
cdfbe: 5
gcdfa: 2
fbcad: 3
dab: 7
cefabd: 9
cdfgeb: 6
eafb: 4
cagedb: 0
ab: 1
Then, the four digits of the output value can be decoded:

cdfeb: 5
fcadb: 3
cdfeb: 5
cdbaf: 3
Therefore, the output value for this entry is 5353.

Following this same process for each entry in the second, larger example above, the output value of each entry can be determined:

fdgacbe cefdb cefbgd gcbe: 8394
fcgedb cgb dgebacf gc: 9781
cg cg fdcagb cbg: 1197
efabcd cedba gadfec cb: 9361
gecf egdcabf bgf bfgea: 4873
gebdcfa ecba ca fadegcb: 8418
cefg dcbef fcge gbcadfe: 4548
ed bcgafe cdgba cbgef: 1625
gbdfcae bgc cg cgb: 8717
fgae cfgab fg bagce: 4315
Adding all of the output values in this larger example produces 61229.

For each entry, determine all of the wire/segment connections and decode the four-digit output values. What do you get if you add up all of the output values?
"""
data = []
set = []
val = "start"
while(val!=[""]):
    val = input()
    val = val.split('|')
    if val != [""]:
        set.append(val[0])
        data.append(val[1])
code = ""
for x in range(len(data)):
    data[x]=data[x].split()
    set[x] = set[x].split()

def decode(i,j, array):
    #print(data[i][j])
    word = list(data[i][j])
    word.sort()
    if len(word) == 2:
        return str(1)
    elif len(word) == 3:
        return str(7)
    elif len(word) == 4:
        return str(4)
    elif len(word) == 7:
        return str(8)
    elif len(word) == 5:
        if len([i for i in word + array[1] if i not in word or i not in array[1]]) == 2:
            return str(3)
        elif len([i for i in word + array[2] if i not in word or i not in array[2]]) == 5:
            return str(2)
        else:
            return str(5)
    elif len(word) == 6:
        if len([i for i in word + array[2] if i not in word or i not in array[2]]) == 2:
            return str(9)
        elif len([i for i in word + array[1] if i not in word or i not in array[1]]) == 3:
            return str(0)
        else:
            return str(6)
    else:
        print("fail")
        return " "

def decode_first(i):
    responses = ['','','','']
    for j in range(10):
        word = list(set[i][j])
        word.sort()
        if len(word) == 2:
            responses[0] = word
        elif len(word) == 3:
            responses[1] = word
        elif len(word) == 4:
            responses[2] = word
        elif len(word) == 7:
            responses[3] = word
    return responses
sum = 0
for x in range(len(data)):
    code = str("")
    array = decode_first(x)
    for y in range(4):
        code += str(decode(x,y, array))

    print(code)
    sum+=int(code)
print(sum)
