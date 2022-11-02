import numpy as np
import re

file = open(r'input\07.txt', 'r')
line = file.readline()
inputdata = np.asarray(re.split(r'\D', line)[:-1], dtype=np.int32)

############################## PART 1 ##############################

median = np.median(inputdata)

fuelcost = np.abs(inputdata - median)

print(f"total fuel cost: {np.sum(fuelcost)}")