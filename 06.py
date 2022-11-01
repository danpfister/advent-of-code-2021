import numpy as np
import re

file = open(r'input\06.txt', 'r')
line = file.readline()
inputdata = np.asarray(re.split(r'\D', line)[:-1], dtype=np.int32)


############################## PART 1 ##############################

currentfish = inputdata
for day in range(80):
    newfish = []
    for fish in currentfish:
        if fish > 0:
            newfish.append(fish - 1)
        else:
            newfish.append(6)
            newfish.append(8)
    currentfish = newfish

print(len(currentfish))

############################## PART 2 ##############################

## setup for c++ test
temp = open(r"input\06_m.txt", "w")
for fish in inputdata:
    temp.write(str(fish) + "\n")
temp.close()