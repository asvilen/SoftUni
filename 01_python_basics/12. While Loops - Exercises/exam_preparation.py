enough = int(input())
task_name = input()

failed = 0
total_score = 0
task_counter = 0
last_task = ""
need_break = False

while task_name != "Enough":
    last_task = task_name
    task_grade = int(input())
    task_counter += 1
    total_score += task_grade

    if task_grade <= 4:
        failed += 1
        if failed == enough:
            need_break = True
            break

    task_name = input()

if not need_break:
    average_grade = total_score / task_counter
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {task_counter}")
    print(f"Last problem: {last_task}")
else:
    print(f"You need a break, {enough} poor grades.")