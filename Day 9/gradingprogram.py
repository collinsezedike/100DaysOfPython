student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
student_grades = {}

# 91 - 100 = Outstanding
# 81 - 90 = Exceeds Expectations
# 71 - 80 = Acceptable
# 70 or lower = Fail


for student in student_scores:
    grade = ''
    if student_scores[student] >= 91:
        grade = "Outstanding"
    elif student_scores[student] >= 81:
        grade = "Exceeds Expectations"
    elif student_scores[student] >= 71:
        grade = "Acceptable"
    else:
        grade = "Fail"

    student_grades[student] = grade

print(student_grades)