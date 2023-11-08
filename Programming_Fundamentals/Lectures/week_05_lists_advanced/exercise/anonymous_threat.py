data = input().split()
input_line = input()
while input_line != '3:1':
    task = input_line.split()
    if 'merge' in task:
        start_index = int(task[1])
        end_index = int(task[2])
        if start_index < 0:
            start_index = 0
        if end_index > (len(data) - 1):
            end_index = len(data) - 1
        merged_elements = ''.join(data[start_index:end_index + 1])
        data[start_index:end_index + 1] = [merged_elements]
    elif 'divide' in task:
        index = int(task[1])
        partitions = int(task[2])
        element = data.pop(index)
        partitions_length = len(element) // partitions
        list1 = []
        for _ in range(partitions - 1):
            list1.append(element[:partitions_length])
            element = element[partitions_length:]
        list1.append(element)
        for current in list1[::-1]:
            data.insert(index, current)
    input_line = input()
print(' '.join(data))
