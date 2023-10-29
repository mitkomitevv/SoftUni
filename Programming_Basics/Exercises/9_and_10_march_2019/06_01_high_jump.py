wanted_height = int(input())
current_height = wanted_height - 30
failed_attempts = 0
jumps = 0
failed = False
while True:
    input_line = int(input())
    jumps += 1

    if input_line > current_height:
        if current_height >= wanted_height:
            print(f"Tihomir succeeded, he jumped over {wanted_height}cm after {jumps} jumps.")
            break
        current_height += 5
        failed_attempts = 0
    else:
        failed_attempts += 1
        if failed_attempts == 3:
            print(f"Tihomir failed at {current_height}cm after {jumps} jumps.")
            break
