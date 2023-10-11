from itertools import chain

task = input()
list1 = []
list2 = []
while task != 'End':
    while task != 'End':
        command = task.split('-')
        list1.append(command)
        task = input()
    for int_element in list1:
        int_element[0] = int(int_element[0])
    list1 = sorted(list1)
    for element in list1:
        del element[0]
    list2 = [element for elements in list1 for element in elements]
    # for elements in list1:
    #     for element in elements:
    #         list2.append(element)
    # list2 = list(chain.from_iterable(list1))
print(list2)
