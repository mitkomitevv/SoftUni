current_year = int(input())

while True:
    current_year += 1
    year_str = str(current_year)
    if len(year_str) == len(set(year_str)):
        print(current_year)
        break
