import numpy as np

data = open(r"input\10.txt", 'r')
lines = [line.strip() for line in data]
raw = np.asarray(lines)

############################## PART 1 ##############################

begin = ['(', '[', '{', '<']
end = [')', ']', '}', '>']
score = {')': 3, ']': 57, '}': 1197, '>': 25137} 
totalscore = 0

for line in raw:
    stack = []
    for char in line:
        if char in begin:
            stack.append(char)
        elif char in end:
            if (popped := stack.pop()) != begin[end.index(char)]:
                print(f"corrupted: expected {end[begin.index(popped)]} got {char}")
                totalscore += score[char]
                break
        else:
            print("something is very wrong")
print(f"total score is: {totalscore}")