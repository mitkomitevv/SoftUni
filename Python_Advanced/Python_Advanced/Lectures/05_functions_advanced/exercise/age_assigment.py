def age_assignment(*names, **kwargs):
    data = []

    for letter, age in kwargs.items():
        for name in names:
            if name.startswith(letter):
                data.append(f"{name} is {age} years old.")
                break
    return '\n'.join(sorted(data))


print(age_assignment("Peter", "George", G=26, P=19))
print()
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
