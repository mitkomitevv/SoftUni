def students_credits(*args):
    courses = []
    result = ""
    total_credits = 0

    for info in args:
        course, credit, max_points, points = info.split('-')
        points_perc = int(points) / int(max_points)
        credits_received = int(credit) * points_perc
        total_credits += credits_received
        courses.append([course, credits_received])

    if total_credits >= 240:
        result += f"Diyan gets a diploma with {total_credits:.1f} credits.\n"
    else:
        result += f"Diyan needs {240 - total_credits:.1f} credits more for a diploma.\n"

    courses = sorted(courses, key=lambda x: -x[1])
    for course, credit in courses:
        result += f"{course} - {credit:.1f}\n"

    return result


print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
