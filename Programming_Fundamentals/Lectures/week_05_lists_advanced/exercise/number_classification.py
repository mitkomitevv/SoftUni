def classification(numbers):
    positive = [x for x in numbers if int(x) >= 0]
    negative = [x for x in numbers if int(x) < 0]
    even = [x for x in numbers if int(x) % 2 == 0]
    odd = [x for x in numbers if int(x) % 2 != 0]
    return f"Positive: {', '.join(positive)}\n" \
           f"Negative: {', '.join(negative)}\n" \
           f"Even: {', '.join(even)}\n" \
           f"Odd: {', '.join(odd)}"


input_line = input().split(', ')
print(classification(input_line))
