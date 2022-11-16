import numpy as np
import re
import cv2 as cv
from matplotlib import pyplot as plt
import random

data = open(r"input\09.txt", 'r')
lines = [line.strip() for line in data]
raw = np.asarray(lines)

inputdata = np.full((102, 102), 9)
for lineindex, line in enumerate(raw):
    for charindex, char in enumerate(line):
        inputdata[lineindex+1][charindex+1] = char

############################## PART 1 ##############################

total = 0
lowpoints = np.zeros(inputdata.shape, dtype=bool)

for x in range(1, 102):
    for y in range(1, 102):
        if inputdata[x][y] < inputdata[x][y-1] and inputdata[x][y] < inputdata[x-1][y] and inputdata[x][y] < inputdata[x][y+1] and inputdata[x][y] < inputdata[x+1][y]:
            total += 1 + inputdata[x][y]
            lowpoints[x][y] = True

print(total)
print(np.sum(lowpoints))

############################## PART 2 ##############################

inputdata = np.array(inputdata*255/9, dtype=np.uint8)
_, inputdata_bin = cv.threshold(inputdata, 235, 255, cv.THRESH_BINARY)

lowpoints = np.array(lowpoints, dtype=np.uint8)
_, lowpoints_bin = cv.threshold(lowpoints, 0.5, 255, cv.THRESH_BINARY)

_, markers = cv.connectedComponents(lowpoints)
markers += 1
markers[inputdata == 255] = 0
inputdata_2 = cv.merge((inputdata_bin, inputdata_bin, inputdata_bin))
markers = cv.watershed(inputdata_2, markers)

for segment in np.unique(markers):
    inputdata_2[markers == segment] = [255 * random.random(), 255 * random.random(), 255 * random.random()]

output = inputdata_2 * 255


cv.imshow("blackwhite", output)
cv.waitKey(0)