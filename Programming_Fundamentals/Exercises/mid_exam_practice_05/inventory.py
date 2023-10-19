def collect(items_list, item):
    if item not in items_list:
        items_list.append(item)
    return items_list

def drop(items_list, item):
    if item in items_list:
        items_list.remove(item)
    return items_list

def combine(items_list, old, new):
    if old in items_list:
        index = items_list.index(old)
        items_list.insert(index + 1, new)
    return items_list

def renew(items_list, item):
    if item in items_list:
        items_list.remove(item)
        items_list.append(item)
    return items_list

def main():
    input_list = input().split(', ')
    input_line2 = input().split(' - ')
    while input_line2[0] != 'Craft!':
        command = input_line2[0]
        item = input_line2[1]
        if command == 'Collect':
            input_list = collect(input_list, item)
        elif command == 'Drop':
            input_list = drop(input_list, item)
        elif command == 'Combine Items':
            old_item, new_item = item.split(':')
            input_list = combine(input_list, old_item, new_item)
        elif command == 'Renew':
            input_list = renew(input_list, item)
        input_line2 = input().split(' - ')
    return ', '.join(input_list)
print(main())
