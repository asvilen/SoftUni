students_grades = {}
number_of_students = int(input())
for student in range(number_of_students):
    name = input()
    grade = float(input())
    if name not in students_grades:
        students_grades[name] = []
    students_grades[name].append(grade)

for student in students_grades:
    average = sum(students_grades[student]) / len(students_grades[student])
    if average >= 4.5:
        print(f"{student} -> {average:.2f}")