file = open(r'input\01.txt')

previous = None
counter = 0

for current in list(file):
    if previous != None:
        if int(current) > previous:
            counter += 1
    previous = int(current)

print(counter)