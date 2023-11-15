def main():
    initial_list = input().split('!')
    input_line2 = input()
    while input_line2 != "Go Shopping!":
        input_line = input_line2.split()
        command = input_line[0]
        if command == 'Urgent':
            urgent(initial_list, input_line[1])
        elif command == 'Unnecessary':
            unnecessary(initial_list, input_line[1])
        elif command == 'Correct':
            correct(initial_list, input_line[1], input_line[2])
        elif command == 'Rearrange':
            rearrange(initial_list, input_line[1])
        input_line2 = input()
    return ', '.join(initial_list)

def urgent(grocery_list, grocery):
    if grocery not in grocery_list:
        grocery_list.insert(0, grocery)

def unnecessary(grocery_list, grocery):
    if grocery in grocery_list:
        grocery_list.remove(grocery)

def correct(grocery_list, old_item, new_item):
    if old_item in grocery_list:
        idx = grocery_list.index(old_item)
        grocery_list[idx] = new_item

def rearrange(grocery_list, grocery):
    if grocery in grocery_list:
        grocery_list.append(grocery)
        grocery_list.remove(grocery)

print(main())
