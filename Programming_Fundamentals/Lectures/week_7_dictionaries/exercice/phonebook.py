info = input()
my_dict = {}
while '-' in info:
    name, number = info.split('-')
    if name not in my_dict:
        my_dict[name] = number
    my_dict[name] = number
    info = input()

n = int(info)
for _ in range(n):
    searched_name = input()
    if searched_name in my_dict:
        print(f"{searched_name} -> {my_dict[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")
