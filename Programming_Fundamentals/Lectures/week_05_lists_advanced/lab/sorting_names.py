def sort_names(names):
    sorted_names = sorted(names, key=lambda x: (-len(x), x))
    return sorted_names


input_names = input().split(', ')
print(sort_names(input_names))



# def sort_names():
#     name = input().split(", ")
#
#     return sorted(name, key=lambda x: (-len(x), x))
#
# print(sort_names())