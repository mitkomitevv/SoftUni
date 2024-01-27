def sorting_cheeses(**kwargs):
    result = ''
    sorted_cheeses = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    for key, value in sorted_cheeses:
        sorted_value = sorted(value, reverse=True)
        result += key + "\n" + '\n'.join(str(x) for x in sorted_value) + '\n'
    return result
