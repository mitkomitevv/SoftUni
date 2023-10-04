n_1 = int(input())
n_2 = int(input())
n_3 = int(input())


def smallest():
    if n_1 < n_2 and n_1 < n_3:
        return n_1
    elif n_2 < n_1 and n_2 < n_3:
        return n_2
    else:
        return n_3


print(smallest())
