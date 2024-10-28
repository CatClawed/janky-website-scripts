import sys

with open('component-codes.txt', 'r') as file:
    for row in file:
        data = row.split('\t')
        s = data[0]
        pos = 0
        for num in data[2].rstrip():
            if num != "2":
                s = s+data[1][pos]
            else:
                s = s+"2"
                #if data[1][pos] != "1":
                #    print(data[1])
            pos = pos + 1
        print(s)