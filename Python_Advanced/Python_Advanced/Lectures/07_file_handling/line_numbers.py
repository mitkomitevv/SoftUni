from string import punctuation


with open('files/text.txt', 'r') as lines:
    text = lines.readlines()

output = open("files/output.txt", "w")

for row in range(len(text)):
    letters_counter = 0
    punctuation_counter = 0
    for el in text[row]:
        if el.isalpha():
            letters_counter += 1
        elif el in punctuation:
            punctuation_counter += 1

    # with open('files/output.txt', 'a') as output:
    #     output.write(f"Line {row + 1}: {text[row][:-1]} ({letters_counter})({punctuation_counter})\n")

    output.write(f"Line {row + 1}: {text[row][:-1] if row + 1 < len(text) else text[row]} "
                 f"({letters_counter})({punctuation_counter})\n")
output.close()
