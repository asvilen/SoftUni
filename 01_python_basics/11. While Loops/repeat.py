student_name = input()

current_year = 1
sum_of_grades = 0
excluded = False
failed = 0

while current_year <= 12:
    grade = float(input())
    if grade < 4:
        failed += 1
        if failed > 1:
            excluded = True
            break
    else:
        sum_of_grades += grade
        current_year += 1

if excluded != True:
    average_grade = sum_of_grades / 12
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
else:
    print(f"{student_name} has been excluded at {current_year} grade")