def multiplication(n1, n2, n3):
    list1 = [n1, n2, n3]
    counter = 0

    for num in list1:
        if num < 0:
            counter += 1

    if n1 == 0 or n2 == 0 or n3 == 0:
        return 'zero'
    if n1 > 0 and n2 > 0 and n3 > 0 or counter == 2:
        return 'positive'
    else:
        return 'negative'


n_1 = int(input())
n_2 = int(input())
n_3 = int(input())
print(multiplication(n_1, n_2, n_3))
