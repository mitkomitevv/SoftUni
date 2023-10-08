grade = float(input())


def grades():
    if grade < 3:
        return 'Fail'
    elif 3.00 <= grade < 3.50:
        return 'Poor'
    elif 3.50 <= grade < 4.50:
        return 'Good'
    elif 4.50 <= grade < 5.50:
        return 'Very Good'
    else:
        return 'Excellent'


print(grades())
