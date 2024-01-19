def add_first(first_set, numbers):
    first_set.update(int(x) for x in numbers)
    return first_set

def add_second(second_set, numbers):
    second_set.update(int(x) for x in numbers)
    return second_set

def remove_first(first_set, numbers):
    for num in numbers:
        first_set.discard(int(num))
    return first_set

def remove_second(second_set, numbers):
    for num in numbers:
        second_set.discard(int(num))
    return second_set

def check_subset(first_set, second_set):
    if first_set.issubset(second_set) or first_set.issuperset(second_set):
        return True
    return False

def printing(first, second):
    print(*sorted(first), sep=', ')
    print(*sorted(second), sep=', ')

def main():
    first_set = set(int(n) for n in input().split())
    second_set = set(int(n) for n in input().split())

    for _ in range(int(input())):
        command = input()

        if 'Add First' in command:
            numbers = command[len('Add First'):].split()
            first_set = add_first(first_set, numbers)
        elif 'Add Second' in command:
            numbers = command[len('Add Second'):].split()
            second_set = add_second(second_set, numbers)
        elif 'Remove First' in command:
            numbers = command[len('Remove First'):].split()
            first_set = remove_first(first_set, numbers)
        elif 'Remove Second' in command:
            numbers = command[len('Remove Second'):].split()
            second_set = remove_second(second_set, numbers)
        elif command == "Check Subset":
            print(check_subset(first_set, second_set))

    printing(first_set, second_set)

if __name__ == '__main__':
    main()
