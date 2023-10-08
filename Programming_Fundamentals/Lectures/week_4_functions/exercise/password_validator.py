def validate(password):
    errors = []
    if len(password) < 6 or len(password) > 10:
        errors.append('Password must be between 6 and 10 characters')
    if not password.isalnum():
        errors.append('Password must consist only of letters and digits')
    counter = 0
    for char in password:
        if char.isdigit():
            counter += 1
    if counter < 2:
        errors.append('Password must have at least 2 digits')
    return errors


input_line = input()
errors_in_password = validate(input_line)
if not errors_in_password:
    print('Password is valid')
else:
    print('\n'.join(errors_in_password))