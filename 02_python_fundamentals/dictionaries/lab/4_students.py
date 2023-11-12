command = input().split(":")
course_info = {}
while len(command) > 1:
    name, student_id, course = command
    if course not in course_info:
        course_info[course] = []
    course_info[course].append([name, student_id])
    command = input().split(":")
course_name = command[0].split("_")
course_name = ' '.join(course_name)
for item in course_info[course_name]:
    print(f"{item[0]} - {item[1]}")