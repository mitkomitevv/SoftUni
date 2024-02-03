import os


def extract_extensions(dir_name, first_level=False):
    for file_name in os.listdir(dir_name):
        file = os.path.join(dir_name, file_name)

        if os.path.isfile(file):
            extension = file_name.split('.')[-1]
            extensions[extension] = extensions.get(extension, []) + [file_name]

        elif os.path.isdir(file) and not first_level:
            extract_extensions(file, first_level=True)


directory = input()
extensions = {}
result = []

try:
    extract_extensions(directory)
except FileNotFoundError:
    print("Directory not found!")

for extension, files in sorted(extensions.items(), key=lambda x: x[0]):
    result.append(f".{extension}")

    for file in sorted(files):
        result.append(f"- - - {file}")

with open("files/report.txt", "w") as report:
    report.write('\n'.join(result))
