people = input().split()
num = int(input())
kill_list = []
index = 0
while len(people) > 0:
    index = (index + num - 1) % len(people)
    kill_list.append(people.pop(index))
print(f"[{','.join(kill_list)}]")
