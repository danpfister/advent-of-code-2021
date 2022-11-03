import numpy as np
import re

file = open(r'input\08.txt', 'r')
lines = [line.strip() for line in file.readlines()]
data_raw = np.asarray(lines)

inputdata = np.empty((200, 14), dtype=object)
for lineindex, line in enumerate(data_raw):
    split = re.split(r'\W+', line)
    for index, signal in enumerate(split):
        inputdata[lineindex][index] = signal

############################## PART 1 ##############################

numberOfDigits = np.zeros((10), dtype=np.int32)

for entry in inputdata:
    for index in range(10, 14):
        match len(entry[index]):
            case 2:
                numberOfDigits[1] += 1
            case 4:
                numberOfDigits[4] += 1
            case 3:
                numberOfDigits[7] += 1
            case 7:
                numberOfDigits[8] += 1
            case _:
                pass

print(f"Number of occurences of digits 1, 4, 7, 8: {np.sum(numberOfDigits)}")