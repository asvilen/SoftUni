student_name = input()

student_grade = 1
grade_sum = 0
is_excluded = False
failed = 0

while student_grade <= 12:
    grade = float(input())
    if grade < 4.00:
        failed += 1
        if failed > 1:
            is_excluded = True
            break
    else:
        grade_sum += grade
        student_grade += 1


if is_excluded == True:
    print(f"{student_name} has been excluded at {student_grade} grade")
else:
    average_grade = grade_sum / 12
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")

