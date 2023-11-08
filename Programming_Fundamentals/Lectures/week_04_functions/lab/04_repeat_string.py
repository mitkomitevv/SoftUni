string = input()
counter = int(input())
# print((lambda x: string * counter)(counter))


def formatted():
    result = string * counter
    return result


print(formatted())
