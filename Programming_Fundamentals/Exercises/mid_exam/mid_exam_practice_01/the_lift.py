waiting = int(input())
flag = False
current_state = [int(x) for x in input().split()]
for i in range(len(current_state)):
    if current_state[i] < 4:
        waiting -= 4 - current_state[i]
        current_state[i] += 4 - current_state[i]
        if waiting == 0:
            flag = True
        if waiting < 0:
            current_state[i] += waiting
            flag = True
            break
if flag and waiting == 0:
    print(*current_state)
elif flag:
    print('The lift has empty spots!')
    print(*current_state)
else:
    print(f"There isn't enough space! {waiting} people in a queue!")
    print(*current_state)
