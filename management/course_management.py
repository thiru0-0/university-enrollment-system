import pandas as pd
import ast

class CourseManagement:
    def __init__(self, course_file="data/courses.csv"):
        self.course_file = course_file
        self._init_course_file()

    def _init_course_file(self):
        """Ensure the CSV file exists with the right columns"""
        try:
            pd.read_csv(self.course_file)  # Try reading file
        except FileNotFoundError:
            df = pd.DataFrame(columns=[
                "course_id", "course_name", "department", "credits",
                "instructor", "semester_offered", "max_enrollment", "student_ids"
            ])
            df.to_csv(self.course_file, index=False)

    def add_course(self, course_data):
        df = pd.read_csv(self.course_file)

        if course_data['course_id'] in df['course_id'].values:
            raise ValueError("Course ID already exists.")

        new_course = pd.DataFrame([course_data])
        df = pd.concat([df, new_course], ignore_index=True)
        df.to_csv(self.course_file, index=False)
        print("Course added successfully.")

    def update_course(self, course_id, updated_data):
        df = pd.read_csv(self.course_file)

        if course_id not in df['course_id'].values:
            print("Course not found.")
            return

        for key, value in updated_data.items():
            if key in df.columns:
                df.loc[df['course_id'] == course_id, key] = value

        df.to_csv(self.course_file, index=False)
        print("Course updated successfully.")

    def delete_course(self, course_id):
        df = pd.read_csv(self.course_file)

        if course_id not in df['course_id'].values:
            print("Course not found.")
            return

        df = df[df['course_id'] != course_id]
        df.to_csv(self.course_file, index=False)
        print("Course deleted successfully.")

    def select_course(self, course_id):
        df = pd.read_csv(self.course_file)
        course = df[df['course_id'] == course_id]

        if course.empty:
            print("Course not found.")
        else:
            print(course.to_string(index=False))

    def list_courses(self):
        df = pd.read_csv(self.course_file)

        if df.empty:
            print("No courses available.")
        else:
            print(df.to_string(index=False))
