minutes = int(input())
seconds = int(input())
length = float(input())
sec_100_m = int(input())

in_seconds = (minutes * 60) + seconds
delay = (length / 120) * 2.5
time = (length / 100) * sec_100_m - delay

diff = abs(in_seconds - time)

if time <= in_seconds:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {time:.3f}.")
else:
    print(f"No, Marin failed! He was {diff:.3f} second slower.")
