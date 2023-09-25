n = int(input())
for _ in range(n):
    string = input()
    if "," in string or "." in string or "_" in string:
        print(f'{string} is not pure!')
    else:
        print(f'{string} is pure.')


# n = int(input())      83 points for some unknown to me reason
# flag = False
# for _ in range(n):
#     string = input()
#     for char in string:
#         if char == ',' or char == '.' or char == '_':
#             flag = True
#             break
#     if flag:
#         print(f'{string} is not pure!')
#     else:
#         print(f'{string} is pure.')
