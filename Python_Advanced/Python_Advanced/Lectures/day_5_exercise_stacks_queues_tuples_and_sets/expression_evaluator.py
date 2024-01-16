from collections import deque

def is_number(s):
    return s.lstrip('-').isdigit() or s.lstrip('+').isdigit()

expression = deque(input().split())
numbers = deque()
result = 0

while expression:
    curr_item = expression.popleft()
    if is_number(curr_item):
        numbers.append(int(curr_item))
    else:
        while len(numbers) > 1:
            if curr_item == '+':
                result = numbers.popleft() + numbers.popleft()
                numbers.appendleft(result)
            elif curr_item == '-':
                result = numbers.popleft() - numbers.popleft()
                numbers.appendleft(result)
            elif curr_item == '*':
                result = numbers.popleft() * numbers.popleft()
                numbers.appendleft(result)
            elif curr_item == '/':
                result = int(numbers.popleft() / numbers.popleft())
                numbers.appendleft(result)

print(result)
