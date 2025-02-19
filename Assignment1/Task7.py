# Task 7
def get_students_with_good_marks(students):
    result = []
    for student in students:
        if (student["mark"] > 80):               # Select students with mark higher than 80
            result.append(student["last name"])  # Get thair last name. Nothing hard.
    return result

# Demonstration
students = [
    {
        "first name": "Harry",
        "last name": "Potter",
        "mark": 79
    },
    {
        "first name": "Hermione",
        "last name": "Granger",
        "mark": 90
    },
    {
        "first name": "Ron",
        "last name": "Weasley",
        "mark": 70
    },
]
print(get_students_with_good_marks(students)) # Expected: ['Granger']