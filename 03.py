import math

file = list(open(r'input\03.txt', 'r'))

gamma = ''

for position in range(len(file[0][:-1])):
    numberOfZeros = 0
    numberOfOnes = 0
    for line in file:
        if line[position] == '0':
            numberOfZeros += 1
        else:
            numberOfOnes += 1
    if numberOfZeros > numberOfOnes:
        gamma += '0'
    else:
        gamma += '1'

gamma = int(gamma, 2) & 0xFFF
epsilon = ~gamma & 0xFFF

print(gamma * epsilon)
