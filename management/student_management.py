import pandas as pd
import ast 

class StudentManagement:
    def __init__(self, student_file="data/students.csv"):
        self.student_file = student_file
        self._init_student_file()

    def _init_student_file(self):
        """Ensure the CSV file exists with the right columns"""
        try:
            pd.read_csv(self.student_file)  # Try reading file
        except FileNotFoundError:
            df = pd.DataFrame(columns=[
                "student_id", "first_name", "last_name",
                "email", "major", "enrollment_year", "gpa","course_ids"
            ])
            df.to_csv(self.student_file, index=False)

    def add_student(self, student_data):
        df = pd.read_csv(self.student_file)

        if student_data['student_id'] in df['student_id'].values:
            raise ValueError("Student ID already exists.")

        new_student = pd.DataFrame([student_data])
        df = pd.concat([df, new_student], ignore_index=True)
        df.to_csv(self.student_file, index=False)
        print("Student added successfully.")

    def update_student(self, student_id, updated_data):
        df = pd.read_csv(self.student_file)

        if student_id not in df['student_id'].values:
            print("Student not found.")
            return

        for key, value in updated_data.items():
            if key in df.columns:
                df.loc[df['student_id'] == student_id, key] = value

        df.to_csv(self.student_file, index=False)
        print("Student updated successfully.")

    def delete_student(self, student_id):
        df = pd.read_csv(self.student_file)

        if student_id not in df['student_id'].values:
            print("Student not found.")
            return

        df = df[df['student_id'] != student_id]
        df.to_csv(self.student_file, index=False)
        print("Student deleted successfully.")

    def select_student(self, student_id):
        df = pd.read_csv(self.student_file)
        student = df[df['student_id'] == student_id]

        if student.empty:
            print("Student not found.")
        else:
            print(student.to_string(index=False))

    def list_students(self):
        df = pd.read_csv(self.student_file)

        if df.empty:
            print("No students available.")
        else:
            print(df.to_string(index=False))