import os
from management.student_management import StudentManagement
from management.course_management import CourseManagement
from management.enrollment_management import EnrollmentManagement
from management.report_management import ReportManagement
from management.ai_recommendation import AIRecommendation
# ...existing imports...


# ------------------ Student Menu ------------------ #
def student_menu(sm):
    while True:
        print("\n--- Student Management ---")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Student by ID")
        print("5. View All Students")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                student_data = {
                    "student_id": int(input("Enter Student ID: ")),
                    "first_name": input("Enter First Name: "),
                    "last_name": input("Enter Last Name: "),
                    "email": input("Enter Email: "),
                    "major": input("Enter Major: "),
                    "enrollment_year": int(input("Enter Enrollment Year: ")),
                    "gpa": float(input("Enter GPA: ")),
                    "course_ids": str([])   # start with empty list
                }
                sm.add_student(student_data)
            except ValueError as e:
                print(e)

        elif choice == "2":
            sid = int(input("Enter Student ID to update: "))
            updated_data = {}

            print("Leave blank if you don’t want to change a field.")
            first_name = input("New First Name: ")
            if first_name: updated_data["first_name"] = first_name

            last_name = input("New Last Name: ")
            if last_name: updated_data["last_name"] = last_name

            email = input("New Email: ")
            if email: updated_data["email"] = email

            major = input("New Major: ")
            if major: updated_data["major"] = major

            enrollment_year = input("New Enrollment Year: ")
            if enrollment_year: updated_data["enrollment_year"] = int(enrollment_year)

            gpa = input("New GPA: ")
            if gpa: updated_data["gpa"] = float(gpa)

            sm.update_student(sid, updated_data)

        elif choice == "3":
            sid = int(input("Enter Student ID to delete: "))
            sm.delete_student(sid)

        elif choice == "4":
            sid = int(input("Enter Student ID to view: "))
            sm.select_student(sid)

        elif choice == "5":
            sm.list_students()

        elif choice == "6":
            break

        else:
            print("Invalid choice. Try again.")

# ------------------ Course Menu ------------------ #
def course_menu(cm):
    while True:
        print("\n--- Course Management ---")
        print("1. Add Course")
        print("2. Update Course")
        print("3. Delete Course")
        print("4. View Course by ID")
        print("5. View All Courses")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            course_data = {
                "course_id": input("Enter Course ID: "),
                "course_name": input("Enter Course Name: "),
                "department": input("Enter Department: "),
                "credits": int(input("Enter Credits: ")),
                "instructor": input("Enter Instructor: "),
                "semester_offered": input("Enter Semester Offered: "),
                "max_enrollment": int(input("Enter Max Enrollment: ")),
                "student_ids": str([])  # start empty
            }
            cm.add_course(course_data)

        elif choice == "2":
            cid = input("Enter Course ID to update: ")
            updated_data = {}
            print("Leave blank if you don’t want to change a field.")

            name = input("New Course Name: ")
            if name: updated_data["course_name"] = name

            dept = input("New Department: ")
            if dept: updated_data["department"] = dept

            credits = input("New Credits: ")
            if credits: updated_data["credits"] = int(credits)

            instructor = input("New Instructor: ")
            if instructor: updated_data["instructor"] = instructor

            semester = input("New Semester Offered: ")
            if semester: updated_data["semester_offered"] = semester

            max_enroll = input("New Max Enrollment: ")
            if max_enroll: updated_data["max_enrollment"] = int(max_enroll)

            cm.update_course(cid, updated_data)

        elif choice == "3":
            cid = input("Enter Course ID to delete: ")
            cm.delete_course(cid)

        elif choice == "4":
            cid = input("Enter Course ID to view: ")
            cm.select_course(cid)

        elif choice == "5":
            cm.list_courses()

        elif choice == "6":
            break
        else:
            print("Invalid choice. Try again.")

# ------------------ Enrollment Menu ------------------ #
def enrollment_menu(em):
    while True:
        print("\n--- Enrollment Management ---")
        print("1. Add Enrollment")
        print("2. Update Enrollment")
        print("3. Delete Enrollment")
        print("4. View Enrollment by ID")
        print("5. View All Enrollments")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            enrollment_data = {
                "enrollment_id": int(input("Enter Enrollment ID: ")),
                "student_id": int(input("Enter Student ID: ")),
                "course_id": input("Enter Course ID: "),
                "status": input("Enter Status (active/completed/pending): "),
                "grade": input("Enter Grade (or leave blank): ")
            }
            em.add_enrollment(enrollment_data)

        elif choice == "2":
            eid = int(input("Enter Enrollment ID to update: "))
            updated_data = {}
            print("Leave blank if you don’t want to change a field.")

            status = input("New Status: ")
            if status: updated_data["status"] = status

            grade = input("New Grade: ")
            if grade: updated_data["grade"] = grade

            em.update_enrollment(eid, updated_data)

        elif choice == "3":
            eid = int(input("Enter Enrollment ID to delete: "))
            em.delete_enrollment(eid)

        elif choice == "4":
            eid = int(input("Enter Enrollment ID to view: "))
            em.select_enrollment(eid)

        elif choice == "5":
            em.list_enrollments()

        elif choice == "6":
            break
        else:
            print("Invalid choice. Try again.")

# ------------------ Report Menu ------------------ #
def report_menu(rm):
    while True:
        print("\n--- Reports ---")
        print("1. Report for a Student")
        print("2. Report for All Students")
        print("3. GPA Leaderboard")
        print("4. Course Popularity Stats")
        print("5. Department Dashboard")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            sid = input("Enter Student ID: ")
            rm.student_course_report(sid)

        elif choice == "2":
            rm.all_students_report()

        elif choice == "3":
            dept = input("Enter Department (or leave blank for all): ")
            rm.gpa_leaderboard(dept if dept else None)

        elif choice == "4":
            rm.course_popularity()

        elif choice == "5":
            rm.department_dashboard()

        elif choice == "6":
            break
        else:
            print("Invalid choice. Try again.")

# ------------------ Main Menu ------------------ #
def main():
    sm = StudentManagement("data/students.csv")
    cm = CourseManagement("data/courses.csv")
    em = EnrollmentManagement("data/enrollments.csv", "data/students.csv", "data/courses.csv")
    rm = ReportManagement("data/students.csv", "data/courses.csv", "data/enrollments.csv")
    # Initialize Groq client from env var if available; otherwise None
    groq_client = None
    try:
        api_key = os.environ.get('GROQ_API_KEY')
        if api_key:
            from groq import Groq
            groq_client = Groq(api_key=api_key)
    except Exception:
        groq_client = None
    ai = AIRecommendation("data/students.csv", "data/courses.csv", "data/enrollments.csv", groq_client)

    while True:
        print("\n--- Main Menu ---")
        print("1. Student Management")
        print("2. Course Management")
        print("3. Enrollment Management")
        print("4. Reports")
        print("5. AI Course Generation (Under Development)")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_menu(sm)
        elif choice == "2":
            course_menu(cm)
        elif choice == "3":
            enrollment_menu(em)
        elif choice == "4":
            report_menu(rm)
        # ...existing code...
        elif choice == "5":
            sid = input("Enter Student ID for AI Recommendation: ")
            ai.get_ai_recommendations(sid)
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
