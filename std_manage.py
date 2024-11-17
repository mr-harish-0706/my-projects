import os
# File paths
STUDENTS_FILE = "students.txt"
RESULTS_FILE = "results.txt"
GRADES_FILE = "grades.txt"

# login credential for admin
admin_ID = "admin101@mrs.edu.in"
admin_pwd = "roja_loves_raja"

#login credential for student
regno = "RA123456789"
std_pwd = "raja_loves_roja"

# List of primary subjects
PRIMARY_SUBJECTS = ["Mathematics","English", "programming", "Biology", "Careear Development"]

# Function to read data from a file and return it as a list of lines
def read_file(file_name):
    if not os.path.exists(file_name):
        return []
    with open(file_name, 'r') as file:
        return file.readlines()

# Function to save data to a file
def write_file(file_name, data):
    with open(file_name, 'a') as file:
        file.write(data + '\n')

# Function to display student information
def display_students():
    students = read_file(STUDENTS_FILE)
    if not students:
        print("No students found.")
    else:
        print("Student List:")
        for student in students:
            print(student.strip())

# Function to add a student
def add_student():
    roll_number = input("Enter roll number: ")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    dob = input("Enter date of birth (YYYY-MM-DD): ")
    email = input("Enter email address: ")

    student_data = f"{roll_number}, {first_name}, {last_name}, {dob}, {email}"
    write_file(STUDENTS_FILE, student_data)
    print(f"Student {first_name} {last_name} added successfully!")

# Function to add results for all 5 subjects
def add_results():
    roll_number = input("Enter roll number: ")
    marks = []
    print(f"        Not Editable        ")
    print(f"Enter marks for the following subjects:")
    for subject in PRIMARY_SUBJECTS:
        mark = input(f"{subject}: ")
        marks.append(mark)

    # Store results in the results file
    result_data = f"{roll_number}, " + ", ".join(marks)
    write_file(RESULTS_FILE, result_data)
    print(f"Results for roll number {roll_number} added successfully.")

# Function to view all results
def view_all_results():
    results = read_file(RESULTS_FILE)
    if not results:
        print("No results found.")
    else:
        print("All Exam Results:")
        for result in results:
            print(result.strip())

# Function to view individual student's results
def view_student_results():
    roll_number = input("Enter roll number: ")
    results = read_file(RESULTS_FILE)
    found = False
    for result in results:
        if result.startswith(roll_number):
            print(result.strip())
            found = True
    if not found:
        print(f"No results found for roll number {roll_number}.")

# Function to calculate grade based on average marks
def calculate_grade(marks):
    marks = [int(m) for m in marks]
    avg_marks = sum(marks) / len(marks)

    if avg_marks >= 90:
        return 'A'
    elif avg_marks >= 75:
        return 'B'
    elif avg_marks >= 50:
        return 'C'
    else:
        return 'D'

# Function to calculate and store grades for each student
def calculate_grades():
    results = read_file(RESULTS_FILE)
    grades = {}

    for result in results:
        data = result.strip().split(", ")
        roll_number = data[0]
        marks = data[1:]

        grade = calculate_grade(marks)
        write_file(GRADES_FILE, f"{roll_number}, {grade}")
        print(f"Grades calculated and stored for roll number {roll_number}.")

# Function to view student's grade
def view_student_grade():
    roll_number = input("Enter roll number: ")
    grades = read_file(GRADES_FILE)
    found = False
    for grade in grades:
        if grade.startswith(roll_number):
            print(grade.strip())
            found = True
    if not found:
        print(f"No grade found for roll number {roll_number}.")

# Main menu for admin operations
def admin_menu():
    Admin_id = input("Enter adminID :")
    Admin_pwd = input("Enter adminpwd :")
    if Admin_id == admin_ID and Admin_pwd == admin_pwd:
        while True:
            print("\n--- Admin Menu ---")
            print("1. Add Student")
            print("2. Add Exam Result")
            print("3. View All Results")
            print("4. View Student's Results")
            print("5. Calculate Grades")
            print("6. View Student's Grade")
            print("7. Exit")
            
            choice = input("Enter your choice: ")

            if choice == "1":
                add_student()
            elif choice == "2":
                add_results()
            elif choice == "3":
                view_all_results()
            elif choice == "4":
                view_student_results()
            elif choice == "5":
                calculate_grades()
            elif choice == "6":
                view_student_grade()
            elif choice == "7":
                break
            else:
                print("Invalid choice, please try again.")
    else :
        print()
        print("---------------- CHECK YOUR CREDENTIALS ! ----------------")
# Main menu for student operations
def student_menu():
    Std_id = input("Enter regester no :")
    Std_pwd = input("Enter password :")
    if Std_id == regno and Std_pwd == std_pwd:
        while True:
            print("\n--- Student Menu ---")
            print("1. View My Results")
            print("2. View My Grade")
            print("3. Exit")
            
            choice = input("Enter your choice: ")

            if choice == "1":
                view_student_results()
            elif choice == "2":
                view_student_grade()
            elif choice == "3":
                break
            else:
                print("Invalid choice, please try again.")

# Main function to choose between admin and student
def main():
    while True:
        print("\n--- MRS Vidhya Peedam ---")
        print("1. Admin")
        print("2. Student")
        print("3. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            admin_menu()
        elif choice == "2":
            student_menu()
        elif choice == "3":
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()