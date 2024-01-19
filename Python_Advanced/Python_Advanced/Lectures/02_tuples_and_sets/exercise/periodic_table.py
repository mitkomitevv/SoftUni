n = int(input())
elements = set()

for _ in range(n):
    element = input().split()
    for el in element:
        elements.add(el)

for element in elements:
    print(element)
