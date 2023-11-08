def which_are_in(first, second):
    my_list = list(filter(lambda x: [y for y in second if x in y], first))
    return my_list


first_string = input().split(', ')
second_string = input().split(', ')
print(which_are_in(first_string, second_string))
