def change(string, char, replacement):
    if char in string:
        string = string.replace(char, replacement)
    return string

def includes(string, substring):
    if substring in string:
        return True
    return False

def end(string, substring):
    if string.endswith(substring):
        return True
    return False

def uppercase(string):
    return string.upper()

def find_index(string, char):
    index = string.index(char)
    return index

def cut(string, start, count):
    string = string[start:start + count]
    return string

def main():
    string = input()
    line = input().split()
    while line[0] != 'Done':
        command = line[0]
        if command == 'Change':
            char, replacement = line[1], line[2]
            string = change(string, char, replacement)
            print(string)
        elif command == 'Includes':
            substring = line[1]
            result = includes(string, substring)
            print(result)
        elif command == 'End':
            substring = line[1]
            result = end(string, substring)
            print(result)
        elif command == 'Uppercase':
            string = uppercase(string)
            print(string)
        elif command == 'FindIndex':
            char = line[1]
            index = find_index(string, char)
            print(index)
        elif command == 'Cut':
            start, count = int(line[1]), int(line[2])
            string = cut(string, start, count)
            print(string)

        line = input().split()

if __name__ == '__main__':
    main()
