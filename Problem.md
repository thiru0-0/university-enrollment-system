# Problem Statement: University Course Enrollment System with AI Recommendations

## Context
Managing course enrollments in a university setting can be a complex and time-consuming task. Students often face challenges in selecting courses that align with their academic goals and prerequisites, while administrators struggle to efficiently manage enrollments and ensure students do not exceed credit limits. Common challenges include:

- **Prerequisite Management:** Students may not be aware of or meet the prerequisites required for certain courses, leading to enrollment issues.
- **Credit Limit Enforcement:** Students might inadvertently exceed the maximum allowable credits per semester, causing academic overload.
- **Manual Enrollment Processes:** Traditional enrollment systems are often manual, prone to errors, and lack real-time validation.
- **Lack of Personalized Recommendations:** Students may not receive tailored course recommendations based on their academic history and goals.
- **Data Management Issues:** Enrollment data is often stored in disparate systems, making it difficult to generate comprehensive reports and insights.

This project aims to develop an intelligent and user-friendly University Course Enrollment System that automates course enrollment, enforces credit limits, checks prerequisites, and offers AI-driven course recommendations tailored to each student's academic profile.

## Problem Description
The goal of this project is to create a Python-based University Course Enrollment System that:

- **Manages Student and Course Data:** Store and retrieve student and course information using CSV files.
- **Enforces Credit Limits:** Ensure students do not exceed the maximum allowable credits per semester.
- **Checks Prerequisites:** Validate that students meet the prerequisites for courses they wish to enroll in.
- **Generates Reports:** Provide detailed enrollment reports for administrative purposes.
- **Integrates AI-driven Recommendations:** Use the Groq AI API to offer personalized course suggestions based on the student's academic history and goals.

## Functional Requirements
### 1. Student Management
- Add new students with details such as student ID, name, program, and total credits.
- Track and manage enrolled courses for each student.

### 2. Course Management
- Add new courses with details such as course ID, title, credits, and prerequisites.
- Store and retrieve course information from CSV files.

### 3. Enrollment Management
- Enroll students in courses after validating prerequisites and credit limits.
- Update student records with enrolled courses and total credits.

### 4. Report Generation
- Generate detailed enrollment reports, including student names, course titles, and credits.
- Save enrollment reports to CSV files for easy retrieval and analysis.

### 5. AI-driven Recommendations
- Fetch personalized course recommendations based on the student’s academic history and goals using Groq AI API.

### 6. Additional Feature Implementation
Implement at least two additional features that enhance the user experience, such as:
- A search feature to locate specific students or courses.
- A visual dashboard for viewing enrollment statistics (total enrollments, average credits per student, etc.).
- A notification system for reminders about enrollment deadlines or course recommendations.

## Technical Details
- **Programming Language:** Python
- **Libraries/Tools:**
  - `groq` for AI-driven suggestions.
  - `pandas` for managing student and course data.
  - `csv` for data persistence.
- **Environment Variables:** The API key for Groq AI must be securely stored in the `GROQ_API_KEY` environment variable.

## Inputs
- **User inputs for student details:**
  - Student ID, Name, Program, Total Credits
- **User inputs for course details:**
  - Course ID, Title, Credits, Prerequisites
- **Menu-driven options for performing actions like:**
  - Adding new students and courses
  - Enrolling students in courses
  - Generating enrollment reports
  - Requesting AI-powered course recommendations

## Outputs
- **Enrollment Summary Reports:**
  - Display detailed enrollment information, including student names, course titles, and credits.
- **Persistent Data Storage:**
  - Save and retrieve student and course details in CSV files.
- **AI-driven Recommendations:**
  - Personalized course suggestions based on the student’s academic history and goals.

## How This Project Solves Key Pain Points
| **Pain Point**                      | **Solution Provided by This Project**                                |
|-------------------------------------|---------------------------------------------------------------------|
| Prerequisite Management            | The system validates prerequisites before enrolling students in courses. |
| Credit Limit Enforcement           | The system ensures students do not exceed the maximum allowable credits. |
| Manual Enrollment Processes        | The system automates enrollment, reducing errors and saving time.    |
| Lack of Personalized Recommendations | AI-powered recommendations ensure students receive tailored course suggestions. |
| Data Management Issues             | CSV-based data storage ensures easy access and tracking of enrollment data. |

## Challenges for Learners
- Implementing a menu-driven user interface for adding, modifying, and viewing data.
- Ensuring accurate validation of prerequisites and credit limits.
- Handling file I/O operations securely, ensuring data integrity when saving/loading CSV files.
- Validating user inputs to ensure accurate data entries.
- Integrating the Groq AI API and handling errors such as network or authentication issues.
- Implementing at least two additional features to improve the overall user experience, such as notifications or enrollment statistics.

## Success Criteria
A successful implementation should:
- Enable efficient course enrollment with prerequisite and credit limit validation.
- Provide detailed enrollment reports that track student enrollments and course details.
- Offer personalized AI-driven course recommendations based on student data.
- Ensure data persistence through CSV storage and retrieval.
- Handle errors gracefully to ensure smooth operation and prevent crashes.
- Include innovative additional features that enhance the user experience or improve the functionality of the system.

## Extension Ideas
- **User Dashboard:** Integrate a visual dashboard to display enrollment statistics, course trends, and student progress.
- **Progress Notifications:** Implement email/SMS notifications for reminders about enrollment deadlines or course recommendations.
- **Multi-User Support:** Allow multiple users (e.g., administrators, students) to access and manage their profiles within the system.

## Notes
- Ensure the Groq API key is stored securely and never hardcoded in the source code.
- Test the system with different sets of student and course data to ensure robustness and accuracy.

This University Course Enrollment System empowers students and administrators to efficiently manage course enrollments, ensuring a smooth and personalized academic experience. 🚀
