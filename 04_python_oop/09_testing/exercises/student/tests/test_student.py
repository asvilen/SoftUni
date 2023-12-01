import unittest

from project.student import Student


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.default_name = 'Genadi'
        self.default_course = "Python"
        self.default_course_notes = ["n1", 'n2']
        self.courses = {self.default_course: self.default_course_notes}
        self.student = Student(self.default_name, self.courses)

    def test_init__when_courses__expect_courses(self):
        self.assertEqual(self.default_name, self.student.name)
        self.assertEqual(self.courses, self.student.courses)

    def test_init__when_not_courses__expect_empty_dict(self):
        student = Student(self.default_name)
        self.assertEqual(self.default_name, student.name)
        self.assertEqual({}, student.courses)

    def test_enroll__when_course_exists__expect_append_new_notes(self):
        new_notes = ['n3', 'n4']
        expected_notes = self.default_course_notes + new_notes
        expected_result = "Course already added. Notes have been updated."
        result = self.student.enroll(self.default_course, new_notes)
        actual_notes = self.student.courses[self.default_course]

        self.assertEqual(expected_result, result)
        self.assertEqual(expected_notes, actual_notes)

    def test_enroll__when_new_course__expect_to_add_course_and_notes(self):
        for ind, command in enumerate(['', 'Y']):
            expected_result = "Course and course notes have been added."
            expected_course = 'JavaScript' + str(ind)
            expected_notes = ['n5', 'n6']
            result = self.student.enroll(expected_course, expected_notes, command)
            self.assertEqual(expected_result, result)
            self.assertTrue(expected_course in self.student.courses)
            self.assertEqual(expected_notes, self.student.courses[expected_course])

    def test_enroll__when_not_add_notes_expect_course_with_no_notes(self):
        expected_result = "Course has been added."
        expected_course = 'JavaScript'
        notes = ['n5', 'n6']
        expected_notes = []
        result = self.student.enroll(expected_course, notes, "N")
        self.assertEqual(expected_result, result)
        self.assertTrue(expected_course in self.student.courses)
        self.assertEqual(expected_notes, self.student.courses[expected_course])

    def test_add_notes__when_course__expect_to_add_notes(self):
        new_note = 'n7'
        expected_new_notes = [x for x in self.default_course_notes]
        expected_new_notes.append(new_note)
        expected = "Notes have been updated"
        result = self.student.add_notes(self.default_course, new_note)
        self.assertEqual(expected, result)
        self.assertEqual(expected_new_notes, self.student.courses[self.default_course])

    def test_add_notes__when_not_course__expect_error(self):
        course = 'JavaScript'
        expected_result = "Cannot add notes. Course not found."
        with self.assertRaises(Exception) as context:
            self.student.add_notes(course, ['n1', 'n2'])
        self.assertEqual(expected_result, str(context.exception))

    def test_leave_course__when_course__expect_to_remove_course(self):
        expected = "Course has been removed"
        result = self.student.leave_course(self.default_course)
        self.assertEqual(expected, result)

    def test_leave_course__when_not_course__expect_error(self):
        course = 'JavaScript'
        expected_result = "Cannot remove course. Course not found."
        with self.assertRaises(Exception) as context:
            self.student.leave_course(course)
        self.assertEqual(expected_result, str(context.exception))

