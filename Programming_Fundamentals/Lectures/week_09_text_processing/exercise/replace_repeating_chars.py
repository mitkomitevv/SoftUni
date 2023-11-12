string = input()
filtered_string = [string[0]] + [string[i] for i in range(len(string)) if string[i] != string[i - 1]]
print(''.join(filtered_string))
