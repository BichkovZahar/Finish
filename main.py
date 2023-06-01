def max1(grades):
    max_grade = max(grades.values())
    max_grade = [student for student, grade in grades.items() if grade == max_grade]
    return max_grade[0]
grades = {}
for i in range(3):
    student = input(f"Введіть імя: ")
    grade = input(f"Введіть оцінку: ")
    grades[student] = grade
print("Студент з найвищою оцінкою:", max1(grades))

