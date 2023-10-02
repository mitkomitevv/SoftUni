number_of_lines = int(input())
checker = ''
flag = False
for _ in range(number_of_lines):
    string = input()
    if string == '(':
        checker += string
    elif string == ')':
        checker += string
    if checker == '()':
        flag = True
if flag:
    print('BALANCED')
else:
    print('UNBALANCED')
