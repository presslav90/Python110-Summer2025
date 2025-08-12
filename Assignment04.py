# ------------------------------------------------------------------------------------------ #
# Title: Assignment04
# Desc: This assignment demonstrates using lists and files to work with data
# Change Log: (Who, When, What)
#   Preslav Angelov, 8/5/2025,Created Script
# ------------------------------------------------------------------------------------------ #


# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
csv_data: str = ''  # Holds combined string data separated by a comma.
file_obj = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.
student_data: list = []
students: list = []

file_obj = open(FILE_NAME, "r")
# Extract the data from the file using a for loop
for row in file_obj.readlines():
    #Transform the data from the file
    student_data = row.strip().split(',')
#    student_data = [student_data[0],student_data[1],student_data[2]]
    students.append(student_data)
file_obj.close()
#print(students)

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        student_first_name = input("Enter the student's first name: ")
        student_last_name = input("Enter the student's last name: ")
        course_name = input("Please enter the name of the course: ")
        csv_data += f"{student_first_name},{student_last_name},{course_name}\n"
        student_data = [student_first_name, student_last_name, course_name]
        students.append(student_data)
        continue

    # Present the current data
    elif menu_choice == "2":
        for student in students:
            print(f"{student[0]},{student[1]},{student[2]}")
        continue

    # Save the data to a file
    elif menu_choice == "3":
        file_obj = open(FILE_NAME, "w")
        for student in students:
            file_obj.write(f"{student[0]},{student[1]},{student[2]}\n")
            print(f"You have registered {student[0]} {student[1]} for {student[2]}.")
        file_obj.close()
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop

    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")
