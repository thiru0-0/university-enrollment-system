import pandas as pd

class AIRecommendation:
    def __init__(self, students_file, courses_file, enrollments_file, groq_client):
        self.students_file = students_file
        self.courses_file = courses_file
        self.enrollments_file = enrollments_file
        self.groq_client = groq_client
        self.courses = self.load_courses()

    def load_courses(self):
        df = pd.read_csv(self.courses_file)
        return df.to_dict(orient='records')

    def get_student(self, student_id):
        df = pd.read_csv(self.students_file)
        student = df[df['student_id'] == int(student_id)]
        if student.empty:
            return None
        return student.iloc[0].to_dict()

    def get_student_enrollments(self, student_id):
        df = pd.read_csv(self.enrollments_file)
        enrollments = df[df['student_id'] == int(student_id)]
        return enrollments.to_dict(orient='records')

    def get_course(self, course_id):
        for course in self.courses:
            if str(course['course_id']) == str(course_id):
                return course
        return None

    def get_ai_recommendations(self, student_id):
        """Get AI-powered course recommendations for a student"""
        student = self.get_student(student_id)
        if not student:
            print(f"Student with ID {student_id} not found.")
            return None

        enrollments = self.get_student_enrollments(student_id)
        enrolled_courses = [self.get_course(e['course_id']) for e in enrollments if self.get_course(e['course_id'])]

        context = f"""
        Student Information:
        - ID: {student['student_id']}
        - Name: {student.get('name', student.get('first_name', '') + ' ' + student.get('last_name', ''))
        }
        - Program: {student.get('program', student.get('major', ''))}
        - Total Credits: {student.get('total_credits', student.get('credits', 'N/A'))}

        Currently Enrolled Courses:
        {', '.join([f"{c['course_id']} ({c.get('title', c.get('course_name', ''))})" for c in enrolled_courses]) if enrolled_courses else 'None'}

        Available Courses:
        {', '.join([f"{c['course_id']} ({c.get('title', c.get('course_name', '') )}, {c.get('credits', 'N/A')} credits)" for c in self.courses])}
        """

        try:
            chat_completion = self.groq_client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "You are an academic advisor helping a university student choose courses. "
                                   "Provide 3-5 relevant course recommendations based on the student's program, "
                                   "currently enrolled courses, and available courses. Consider prerequisites and "
                                   "logical progression in their academic journey. Format your response with clear "
                                   "bullet points and brief explanations for each recommendation."
                    },
                    {
                        "role": "user",
                        "content": f"Please provide course recommendations for this student:\n{context}"
                    }
                ],
                model="llama-3.1-8b-instant",
                temperature=0.7,
                max_tokens=500
            )

            recommendations = chat_completion.choices[0].message.content
            print(f"AI Recommendations for {student.get('name', student.get('first_name', '') + ' ' + student.get('last_name', ''))}:\n")
            print(recommendations)
            return recommendations

        except Exception as e:
            print(f"Error getting AI recommendations: {e}")