import os
import check
from file import student_file

def add_student():
    if not os.path.exists(student_file):#check if file exists
        with open(student_file, "w") as file:
            pass
        
    os.system('cls' if os.name == 'nt' else 'clear')#clear screen
    print("➕🧑‍🎓 ADD STUDENT\n")

    while True:
        student_id = input("🔹 Student Id (8 digits) or 'B' to go back : ")#asking user for student id
        if student_id.upper() == 'B':#if user enter 'B' then return to main menu
            return
        if not student_id.isdigit():#check if student id is in numbers
            print("❌ ERROR! Student ID has to be in numbers.\n")
            continue
        if len(str(student_id)) != 8:#check if student id is 8 digits
            print("❌ ERROR: Student Id has to be exactly 8 digits\n")
            continue
        if check.student_exists(student_id):#check if student id exists
            print("❌ ERROR: Student Id already exists.\n")
            continue

        student_name = input("🔹 Student Name (First letter capital) or 'B' to go back : ")#askng user for student name
        if student_name.upper() == 'B':#if user enter 'B' then return to main menu
            return
        if student_name.isdigit():#check if student name is in numbers
            print("❌ ERROR: Invalid student name.\n")
            continue
        if not student_name[0].isupper():#check if first letter of student name is in capital
            print("❌ ERROR: First letter has to be in capital letter.\n")
            continue
        if not all(x.isalpha() or x.isspace() for x in student_name):#check if student name is in alphabets and spaces
            print("❌ ERROR: Invalid student name.\n")
            continue

        student_contact = input("🔹 Student Contact or 'B' to go back : ")#asking user for student contact number
        if student_contact.upper() == 'B': #if user enter 'B' then return to main menu
            return
        if not (7<= len(student_contact) <= 15):#check if student contact is between 7 to 15 digits
            print("❌ ERROR: Contact must be only 7 to 15 digits.\n")
            continue
        if not student_contact.isdigit():#check if student contact is in numbers
            print("❌ ERROR: Contact invalid.\n")
            continue
        break
    with open (student_file, 'a') as file:
        file.write(f"{student_id},{student_name},{student_contact}\n")#storing the data user enter to the student file
    print("✅ Student added successfully.\n")