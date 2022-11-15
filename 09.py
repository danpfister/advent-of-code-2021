import numpy as np
import re

data = open(r"input\09.txt", 'r')
lines = [line.strip() for line in data]
raw = np.asarray(lines)

inputdata = np.full((102, 102), 9)
for lineindex, line in enumerate(raw):
    for charindex, char in enumerate(line):
        inputdata[lineindex+1][charindex+1] = char

############################## PART 1 ##############################

total = 0

for x in range(1, 102):
    for y in range(1, 102):
        if inputdata[x][y] < inputdata[x][y-1] and inputdata[x][y] < inputdata[x-1][y] and inputdata[x][y] < inputdata[x][y+1] and inputdata[x][y] < inputdata[x+1][y]:
            total += 1 + inputdata[x][y]

print(total)