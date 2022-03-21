import sys
import re

# Attempts to insert the missing numbers from a list of enums.
# It definitely doesn't get all of them, but the numbers are better now.
# May make mistakes, double check what it inserts, probably the most jank of the jank scripts.

prev = 0

with open('list.txt') as f:
    for line in f:
        if line:
            results = re.findall(r'\d+', line)
            if results:
                if prev > int(results[0]):
                    prev = 0
                if prev+1 < int(results[0]):
                    while prev is not int(results[0]):
                        prev = prev+1
                        num = len(results[0])
                        print(line[:-(num+1)]+str(prev).zfill(num))
                else:
                    print(line.rstrip())
                prev = int(results[0])
            else:
                prev = 0
                print(line.rstrip())