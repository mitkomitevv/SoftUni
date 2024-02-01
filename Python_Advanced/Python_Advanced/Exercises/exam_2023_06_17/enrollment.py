def gather_credits(needed, *args):
    courses, current_credits = [], 0

    for course, credit in args:
        if current_credits < needed:
            if course not in courses:
                current_credits += credit
                courses.append(course)
        else:
            break

    if current_credits >= needed:
        return f"Enrollment finished! Maximum credits: {current_credits}.\nCourses: {', '.join(sorted(courses))}"
    return f"You need to enroll in more courses! You have to gather {needed - current_credits} credits more."

print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
