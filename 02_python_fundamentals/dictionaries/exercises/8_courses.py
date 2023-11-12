courses = {}
while True:
    command = input().split(" : ")
    if len(command) == 1:
        break
    course_name, student_name = command[0], command[1]
    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)

for course in courses:
    print(f"{course}: {len(courses[course])}")
    for name in courses[course]:
        print(f"-- {name}")