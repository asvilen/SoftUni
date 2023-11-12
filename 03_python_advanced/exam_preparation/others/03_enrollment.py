def gather_credits(needed_credit, *args):
    gained_credits = 0
    taken_courses = []
    for course, credit in args:
        if gained_credits >= needed_credit:
            break
        if course not in taken_courses:
            taken_courses.append(course)
            gained_credits += credit
    if gained_credits >= needed_credit:
        message = f"Enrollment finished! Maximum credits: {gained_credits}.\nCourses: {', '.join(sorted(taken_courses))}"
    else:
        message = f"You need to enroll in more courses! You have to gather {needed_credit - gained_credits} credits more."
    return message

# def gather_credits(needed_credit, *args):
#     gained_credits = 0
#     taken_courses = []
#     success = False
#     for course, credit in args:
#         if course not in taken_courses:
#             taken_courses.append(course)
#             gained_credits += credit
#         if gained_credits >= needed_credit:
#             success = True
#             break
#     if success:
#         message = f"Enrollment finished! Maximum credits: {gained_credits}.\nCourses: {', '.join(sorted(taken_courses))}"
#     else:
#         message = f"You need to enroll in more courses! You have to gather {needed_credit - gained_credits} credits more."
#     return message

# Example usage:
print(gather_credits(80, ("Basics", 27)))
print(gather_credits(80, ("Advanced", 30), ("Basics", 27), ("Fundamentals", 27)))
print(gather_credits(60, ("Basics", 27), ("Fundamentals", 27), ("Advanced", 30), ("Web", 30)))

