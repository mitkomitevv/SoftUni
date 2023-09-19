length = int(input())
width = int(input())
height = int(input())
percentage = float(input())

volume = length * width * height
volume_in_lt = volume / 1000
space_took = percentage / 100

total_lt = volume_in_lt - (volume_in_lt * space_took)

print(total_lt)