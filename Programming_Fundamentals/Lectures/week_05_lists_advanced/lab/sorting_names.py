def sort_names(names):
    sorted_names = sorted(names, key=lambda x: (-len(x), x))
    return sorted_names


input_names = input().split(', ')
print(sort_names(input_names))
