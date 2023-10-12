def classification(numbers):
    positive = [int(x) for x in numbers if int(x) >= 0]
    negative = [int(x) for x in numbers if int(x) < 0]
    even = [int(x) for x in numbers if int(x) % 2 == 0]
    odd = [int(x) for x in numbers if int(x) % 2 != 0]
    return f"Positive: {', '.join(map(str, positive))}\n" \
           f"Negative: {', '.join(map(str, negative))}\n" \
           f"Even: {', '.join(map(str, even))}\n" \
           f"Odd: {', '.join(map(str, odd))}"


input_line = input().split(', ')
print(classification(input_line))
