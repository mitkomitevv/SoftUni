def group_of_tens(numbers):
    copy_list = numbers.copy()
    group1 = 0
    group2 = 10
    while len(numbers) > 0:
        list1 = []
        for number in copy_list:
            if group1 < number <= group2:
                list1.append(number)
                numbers.remove(number)
        print(f"Group of {group2}'s: {list1}")
        group1 += 10
        group2 += 10


input_line = list(map(int, input().split(', ')))
group_of_tens(input_line)
