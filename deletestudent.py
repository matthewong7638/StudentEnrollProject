import os
from file import student_file

def delete_student():#delete student function
    print("✍️ DELETE STUDENT\n")
    while True:
        student_id = input("🔹 Student ID to delete or 'B' to go back : ").strip()#asking user for student id to delete
        if student_id.upper() == 'B':#if user enter 'B' then return to main menu
            return

        if not os.path.exists(student_file):#check if file exists
            print("❌ ERROR: Student file does not exist.\n")
            return

        with open(student_file, 'r') as file:
            lines = file.readlines()#reading the lines in the file

        with open(student_file, 'w') as file:#open file in write mode
            student_found = False#initializing student found to False
            for line in lines:
                if line.strip().split(',')[0] != student_id:#splitting the line and checking if student id exists
                    file.write(line)#writing the line to the file
                else:
                    student_found = True#setting student found to True

        if student_found:
            print(f"❌ ERROR: Student with ID {student_id} has been deleted.\n")#if student found then print this message
        else:
            print(f"❌ ERROR: Student with ID {student_id} not found.\n")#if student not found then print this message