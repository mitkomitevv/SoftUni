def naughty_or_nice_list(kids, *args, **kwargs):
    all_kids = {'Nice': [], 'Naughty': [], 'Not found': []}

    for info in args:
        num, naughty_or_nice = info.split('-')
        num = int(num)
        if sum(1 for kid in kids if kid[0] == num) == 1:
            for i, data in enumerate(kids):
                if data[0] == num:
                    all_kids[naughty_or_nice].append(data[1])
                    del kids[i]

    if kwargs:
        for name, info in kwargs.items():
            if sum(1 for x in kids if x[1] == name) == 1:
                for i, data in enumerate(kids):
                    if name == data[1]:
                        all_kids[info].append(name)
                        del kids[i]

    all_kids['Not found'].extend(name for n, name in kids)

    result = []
    for info, names in all_kids.items():
        if names:
            result.append(f"{info}: {', '.join(names)}")

    return '\n'.join(result)


print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
