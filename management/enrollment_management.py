import pandas as pd
import ast
from datetime import datetime

class EnrollmentManagement:
    def __init__(self, enrollment_file="data/enrollments.csv", student_file="data/students.csv", course_file="data/courses.csv"):
        self.enrollment_file = enrollment_file
        self.student_file = student_file
        self.course_file = course_file
        self._init_enrollment_file()

    def _init_enrollment_file(self):
        """Ensure the enrollment CSV file exists with the right columns"""
        try:
            pd.read_csv(self.enrollment_file)
        except FileNotFoundError:
            df = pd.DataFrame(columns=[
                "enrollment_id", "student_id", "course_id",
                "enrollment_date", "status", "grade"
            ])
            df.to_csv(self.enrollment_file, index=False)

    def add_enrollment(self, enrollment_data):
        enrollments = pd.read_csv(self.enrollment_file)
        students = pd.read_csv(self.student_file)
        courses = pd.read_csv(self.course_file)

        # Validate student and course existence
        student_id = enrollment_data['student_id']
        course_id = enrollment_data['course_id']

        if student_id not in students['student_id'].values:
            print("Student not found.")
            return
        if course_id not in courses['course_id'].values:
            print("Course not found.")
            return

        # Check course capacity
        course_row = courses[courses['course_id'] == course_id].iloc[0]
        enrolled_students = ast.literal_eval(course_row['student_ids']) if pd.notna(course_row['student_ids']) else []
        if len(enrolled_students) >= int(course_row['max_enrollment']):
            print("Course is full. Cannot enroll student.")
            return

        # Check duplicate enrollment
        if not enrollments[(enrollments['student_id'] == student_id) & (enrollments['course_id'] == course_id)].empty:
            print("Student already enrolled in this course.")
            return

        # Add enrollment record
        enrollment_data['enrollment_date'] = datetime.now().strftime("%Y-%m-%d")
        new_enrollment = pd.DataFrame([enrollment_data])
        enrollments = pd.concat([enrollments, new_enrollment], ignore_index=True)
        enrollments.to_csv(self.enrollment_file, index=False)

        # Update student course_ids
        student_idx = students[students['student_id'] == student_id].index[0]
        student_courses = ast.literal_eval(students.at[student_idx, 'course_ids']) if pd.notna(students.at[student_idx, 'course_ids']) else []
        student_courses.append(course_id)
        students.at[student_idx, 'course_ids'] = str(student_courses)
        students.to_csv(self.student_file, index=False)

        # Update course student_ids
        course_idx = courses[courses['course_id'] == course_id].index[0]
        enrolled_students.append(student_id)
        courses.at[course_idx, 'student_ids'] = str(enrolled_students)
        courses.to_csv(self.course_file, index=False)

        print("Enrollment added successfully.")

    def update_enrollment(self, enrollment_id, updated_data):
        enrollments = pd.read_csv(self.enrollment_file)

        if enrollment_id not in enrollments['enrollment_id'].values:
            print("Enrollment not found.")
            return

        for key, value in updated_data.items():
            if key in enrollments.columns:
                enrollments.loc[enrollments['enrollment_id'] == enrollment_id, key] = value

        enrollments.to_csv(self.enrollment_file, index=False)
        print("Enrollment updated successfully.")

    def delete_enrollment(self, enrollment_id):
        enrollments = pd.read_csv(self.enrollment_file)
        students = pd.read_csv(self.student_file)
        courses = pd.read_csv(self.course_file)

        enrollment = enrollments[enrollments['enrollment_id'] == enrollment_id]

        if enrollment.empty:
            print("Enrollment not found.")
            return

        student_id = enrollment.iloc[0]['student_id']
        course_id = enrollment.iloc[0]['course_id']

        # Remove from enrollments
        enrollments = enrollments[enrollments['enrollment_id'] != enrollment_id]
        enrollments.to_csv(self.enrollment_file, index=False)

        # Update student course_ids
        student_idx = students[students['student_id'] == student_id].index[0]
        student_courses = ast.literal_eval(students.at[student_idx, 'course_ids']) if pd.notna(students.at[student_idx, 'course_ids']) else []
        if course_id in student_courses:
            student_courses.remove(course_id)
        students.at[student_idx, 'course_ids'] = str(student_courses)
        students.to_csv(self.student_file, index=False)

        # Update course student_ids
        course_idx = courses[courses['course_id'] == course_id].index[0]
        enrolled_students = ast.literal_eval(courses.at[course_idx, 'student_ids']) if pd.notna(courses.at[course_idx, 'student_ids']) else []
        if student_id in enrolled_students:
            enrolled_students.remove(student_id)
        courses.at[course_idx, 'student_ids'] = str(enrolled_students)
        courses.to_csv(self.course_file, index=False)

        print("Enrollment deleted successfully.")

    def select_enrollment(self, enrollment_id):
        enrollments = pd.read_csv(self.enrollment_file)
        enrollment = enrollments[enrollments['enrollment_id'] == enrollment_id]

        if enrollment.empty:
            print("Enrollment not found.")
        else:
            print(enrollment.to_string(index=False))

    def list_enrollments(self):
        enrollments = pd.read_csv(self.enrollment_file)

        if enrollments.empty:
            print("No enrollments available.")
        else:
            print(enrollments.to_string(index=False))
