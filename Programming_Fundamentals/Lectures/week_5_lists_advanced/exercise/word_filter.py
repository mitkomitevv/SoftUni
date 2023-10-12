def even_length(words):
    list1 = [x for x in words if len(x) % 2 == 0]
    return list1


input_line = input().split()
same_length = even_length(input_line)
print('\n'.join(same_length))
