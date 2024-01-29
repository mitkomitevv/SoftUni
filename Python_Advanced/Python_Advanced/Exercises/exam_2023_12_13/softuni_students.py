def softuni_students(*args, **kwargs):
    invalid_course_students = []
    valid_course_students = {}
    result = []

    for student in args:
        student_id, name = student
        if student_id in kwargs:
            valid_course_students[name] = kwargs[student[0]]
        else:
            invalid_course_students.append(name)

    sorted_students = dict(sorted(valid_course_students.items()))

    for key, value in sorted_students.items():
        result.append(f"*** A student with the username {key} has successfully finished the course {value}!")

    if invalid_course_students:
        result.append(f"!!! Invalid course students: {', '.join(sorted(invalid_course_students))}")

    return '\n'.join(result)


print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))
