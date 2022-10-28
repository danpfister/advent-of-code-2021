import numpy as np
import re

file = open(r'input\05.txt', 'r')
lines = [line.strip() for line in file.readlines()]
data_raw = np.asarray(lines)

data = np.empty((500, 4), dtype=np.int32)
for lineindex, line in enumerate(data_raw):
    split = re.split(r'\D+', line)
    for axis, coordinate in enumerate(split):
        data[lineindex][axis] = int(coordinate)

print(data)


############################## PART 1 ##############################