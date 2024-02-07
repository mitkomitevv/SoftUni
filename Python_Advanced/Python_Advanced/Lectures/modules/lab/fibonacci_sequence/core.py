def create_sequence(n):
    seq = [0, 1]

    for _ in range(1, n - 1):
        seq.append(seq[-1] + seq[-2])

    print(*seq)
    return seq

def locate_number(seq, num):
    try:
        print(f"The number - {num} is at index {seq.index(num)}")
    except ValueError:
        print(f"The number {num} is not in the sequence")
