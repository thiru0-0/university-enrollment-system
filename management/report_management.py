import pandas as pd
import ast

class ReportManagement:
    def __init__(self, student_file="data/students.csv", course_file="data/courses.csv", enrollment_file="data/enrollments.csv"):
        self.student_file = student_file
        self.course_file = course_file
        self.enrollment_file = enrollment_file

    def student_course_report(self, student_id=None):
        students = pd.read_csv(self.student_file)
        courses = pd.read_csv(self.course_file)
        enrollments = pd.read_csv(self.enrollment_file)

        if students.empty:
            print("No students found.")
            return

        if courses.empty:
            print("No courses found.")
            return

        if enrollments.empty:
            print("No enrollments found.")
            return

        if student_id:
            students = students[students['student_id'] == student_id]
            if students.empty:
                print("Student not found.")
                return

        for _, student in students.iterrows():
            s_id = student['student_id']
            full_name = f"{student['first_name']} {student['last_name']}"
            gpa = student['gpa']

            # Find student enrollments
            enrolled_courses = enrollments[enrollments['student_id'] == s_id]

            course_names = []
            for _, enr in enrolled_courses.iterrows():
                course_id = enr['course_id']
                course = courses[courses['course_id'] == course_id]
                if not course.empty:
                    course_names.append(course.iloc[0]['course_name'])

            print("\n--- Student Report ---")
            print(f"ID: {s_id}")
            print(f"Name: {full_name}")
            print(f"GPA: {gpa}")
            print(f"Courses: {', '.join(course_names) if course_names else 'None'}")

    def all_students_report(self):
        """Generate reports for all students"""
        self.student_course_report()
