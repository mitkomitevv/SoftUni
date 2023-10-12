def palindrome(words):
    return [x for x in input_line if x == x[::-1]]


input_line = input().split()
word = input()
pal_list = palindrome(input_line)
pal_count = pal_list.count(word)
print(pal_list)
print(f'Found palindrome {pal_count} times')
