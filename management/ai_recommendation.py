import os
import json
import pandas as pd

class AIRecommendation:
    def __init__(self, students_file, courses_file, enrollments_file, groq_client):
        self.students_file = students_file
        self.courses_file = courses_file
        self.enrollments_file = enrollments_file
        self.groq_client = groq_client or self._init_groq_client()
        self.courses = self.load_courses()

    def _init_groq_client(self):
        """Initialize Groq client from GROQ_API_KEY if available; otherwise return None."""
        try:
            api_key = os.environ.get('GROQ_API_KEY')
            if not api_key:
                return None
            from groq import Groq
            return Groq(api_key=api_key)
        except Exception:
            return None

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
        """Return course recommendations as a list of {course_id, course_name}.

        If a Groq client is configured, ask the model to rank and return only course IDs
        (JSON array). Otherwise, fall back to a simple list of courses the student is not
        yet enrolled in.
        """
        student = self.get_student(student_id)
        if not student:
            print(f"Student with ID {student_id} not found.")
            return []

        enrollments = self.get_student_enrollments(student_id)
        enrolled_ids = {str(e['course_id']) for e in enrollments}

        # Candidate courses: not yet enrolled
        candidate_courses = [c for c in self.courses if str(c.get('course_id')) not in enrolled_ids]

        # If Groq client is present, ask it to rank the candidate course IDs.
        if self.groq_client and candidate_courses:
            try:
                candidate_ids = [str(c.get('course_id')) for c in candidate_courses]
                candidate_lines = "\n".join(
                    f"- {c.get('course_id')} | {c.get('course_name', c.get('title', ''))} | {c.get('credits', 'N/A')} credits"
                    for c in candidate_courses
                )

                prompt = (
                    "You are an academic advisor. Given the student's info and candidate courses, "
                    "return ONLY a JSON array of up to 5 course_ids (strings), ranked by relevance. "
                    "Do not include any text before or after the JSON.\n\n"
                    f"Student Major: {student.get('major', '')}\n"
                    f"GPA: {student.get('gpa', '')}\n"
                    f"Currently Enrolled IDs: {sorted(list(enrolled_ids))}\n\n"
                    "Candidate Courses (id | name | credits):\n"
                    f"{candidate_lines}\n\n"
                    "Return JSON only, example: [\"CS101\", \"MATH201\"]"
                )

                chat_completion = self.groq_client.chat.completions.create(
                    messages=[
                        {"role": "user", "content": prompt},
                    ],
                    model="llama-3.1-8b-instant",
                    temperature=0.2,
                    max_tokens=200,
                )

                content = chat_completion.choices[0].message.content if chat_completion.choices else "[]"
                try:
                    selected_ids = json.loads(content)
                    if not isinstance(selected_ids, list):
                        selected_ids = []
                except Exception:
                    selected_ids = []

                # Map selected IDs to recommendations; fallback to first few candidates if empty
                selected_set = {str(x) for x in selected_ids}
                selected_courses = [c for c in candidate_courses if str(c.get('course_id')) in selected_set]
                if not selected_courses:
                    selected_courses = candidate_courses[:5]

                recommendations = [
                    {
                        'course_id': c.get('course_id'),
                        'course_name': c.get('course_name', c.get('title', ''))
                    }
                    for c in selected_courses
                ]

                for rec in recommendations:
                    print(f"{rec['course_id']} - {rec['course_name']}")

                return recommendations
            except Exception:
                # On any AI error, fall back to simple heuristic below
                pass

        # Fallback: simple list of not-yet-enrolled courses
        recommendations = []
        for course in candidate_courses:
            recommendations.append({
                'course_id': course.get('course_id'),
                'course_name': course.get('course_name', course.get('title', ''))
            })

        for rec in recommendations:
            print(f"{rec['course_id']} - {rec['course_name']}")

        return recommendations