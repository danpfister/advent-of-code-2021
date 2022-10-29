import numpy as np
import re

file = open(r'input\05.txt', 'r')
lines = [line.strip() for line in file.readlines()]
data_raw = np.asarray(lines)

inputdata = np.empty((500, 4), dtype=np.int32)
for lineindex, line in enumerate(data_raw):
    split = re.split(r'\D+', line)
    for axis, coordinate in enumerate(split):
        inputdata[lineindex][axis] = int(coordinate)




############################## PART 1 ##############################

field = np.zeros((1000, 1000))
for input in inputdata:
    x1, y1, x2, y2 = input[0], input[1], input[2], input[3]
    if x1 == x2:
        direction = 1 if y2 > y1 else -1
        for y in range(y1, y2 + direction, direction):
            field[x1][y] += 1
    if y1 == y2:
        direction = 1 if x2 > x1 else -1
        for x in range(x1, x2 + direction, direction):
            field[x][y1] += 1

print(f"Number of points where at least two lines overlap: {len(np.argwhere(field >= 2))}")