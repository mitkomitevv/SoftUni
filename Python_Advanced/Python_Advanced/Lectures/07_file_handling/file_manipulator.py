import os
from os import remove

input_line = input().split('-')
while input_line[0] != 'End':
    command, file_name, *data = input_line

    if command == 'Create':
        with open(f"files/{file_name}", "w"): pass

    elif command == 'Add':
        content = data[0]
        with open(f"files/{file_name}", "a") as file:
            file.write(f"{content}\n")

    elif command == 'Replace':
        old, new = data
        try:
            with open(f"files/{file_name}", "r+") as file:
                text = file.read().replace(old, new)
                file.seek(0)
                file.write(text)
                file.truncate()
        except FileNotFoundError:
            print("An error occurred")

    elif command == 'Delete':
        try:
            os.remove(f"files/{file_name}")
        except FileNotFoundError:
            print("An error occurred")

    input_line = input().split('-')