import os
import django
from datetime import date, datetime

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from main_app.models import Student


def add_students() -> None:
    std_1 = Student(
        student_id='FC5204',
        first_name='John',
        last_name='Doe',
        birth_date=datetime(1995, 5, 15),
        email='john.doe@university.com',
    )
    std_2 = Student(
        student_id='FE0054',
        first_name='Jane',
        last_name='Smith',
        birth_date=None,
        email='jane.smith@university.com',
    )
    std_3 = Student(
        student_id='FH2014',
        first_name='Alice',
        last_name='Johnson',
        birth_date=datetime(1998, 2, 10),
        email='alice.johnson@university.com',
    )
    std_4 = Student(
        student_id='FH2015',
        first_name='Bob',
        last_name='Wilson',
        birth_date=datetime(1996, 11, 25),
        email='bob.wilson@university.com',
    )
    Student.objects.bulk_create([std_1, std_2, std_3, std_4])


def get_students_info():
    # "Student №{student_id}: {first_name} {last_name}; Email: {email}
    result_list = []
    students = Student.objects.all()
    for student in students:
        result_list.append(
            f"Student №{student.student_id}: {student.first_name} {student.last_name}; Email: {student.email}"
        )
    return '\n'.join(result_list)


def update_students_emails():
    students = Student.objects.all()
    for student in students:
        student.email = student.email.split("@")[0] + '@' + 'uni-students.com'
        student.save()


def truncate_students():
    Student.objects.all().delete()


truncate_students()
print(Student.objects.all())
print(f"Number of students: {Student.objects.count()}")