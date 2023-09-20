page_count = int(input())
pages_in_hour = int(input())
days = int(input())

total_reading = page_count // pages_in_hour
hours_day = total_reading / days

print(hours_day)