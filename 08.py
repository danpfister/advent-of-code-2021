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

############################## PART 2 ##############################

letters = 'abcdefg'

for entry in inputdata:
    configuration = {}
    lettercount = {}
    # count occurence of each signal
    for letter in letters:
        count = 0
        for index in range(10):
            if letter in entry[index]:
                count += 1
        lettercount[letter] = count
    # signal with 4 occurences is segment 4,
    # signal with 6 occurences is segment 1,
    # signal with 8 occurences is segment 2
    # and signal with 9 occurences is segment 5
    for signal, count in lettercount.items():
        match count:
            case 4:
                configuration[signal] = 4
            case 6:
                configuration[signal] = 1
            case 9:
                configuration[signal] = 5
            case _:
                pass
    print(configuration )