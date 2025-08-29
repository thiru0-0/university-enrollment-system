from management.student_management import StudentManagement

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
                    "course_ids": input("Enter Course IDs (comma separated): ").split(",")
                }
                sm.add_student(student_data)
            except ValueError as e:
                print(e)

        elif choice == "2":
            sid = int(input("Enter Student ID to update: "))
            updated_data = {}

            print("Leave blank if you don’t want to change a field.")
            first_name = input("New First Name: ")
            if first_name:
                updated_data["first_name"] = first_name

            last_name = input("New Last Name: ")
            if last_name:
                updated_data["last_name"] = last_name

            email = input("New Email: ")
            if email:
                updated_data["email"] = email

            major = input("New Major: ")
            if major:
                updated_data["major"] = major

            enrollment_year = input("New Enrollment Year: ")
            if enrollment_year:
                updated_data["enrollment_year"] = int(enrollment_year)

            gpa = input("New GPA: ")
            if gpa:
                updated_data["gpa"] = float(gpa)

            course_ids = input("New Course IDs (comma separated): ")
            if course_ids:
                updated_data["course_ids"] = course_ids.split(",")

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


def main():
    sm = StudentManagement("data/students.csv")

    while True:
        print("\n--- Main Menu ---")
        print("1. Student Management")
        print("2. Course Management")
        print("3. Enrollment Management")
        print("4. Reports")
        print("5. AI Course Generation")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_menu(sm)

        elif choice == "2":
            print("⚡ Course Management - To be implemented")

        elif choice == "3":
            print("⚡ Enrollment Management - To be implemented")

        elif choice == "4":
            print("⚡ Reports - To be implemented")

        elif choice == "5":
            print("⚡ AI Course Generation - To be implemented")

        elif choice == "6":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
