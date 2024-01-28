def kwargs_length(**dicts):
    return len(dicts)


dictionary = {'name': 'Peter', 'age': 25}

print(kwargs_length(**dictionary))

print()

dictionary = {}

print(kwargs_length(**dictionary))
