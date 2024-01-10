from collections import deque

string = input()
indexes = deque()

for i in range(len(string)):
    if string[i] == '(':
        indexes.append(i)
    elif string[i] == ')':
        print(string[indexes.pop():i+1])
