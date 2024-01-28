def even_odd(*args):
    even_or_odd = args[-1]
    if even_or_odd == 'even':
        return [int(x) for x in args[:-1] if x % 2 == 0]
    return [int(x) for x in args[:-1] if x % 2 != 0]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print()
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
