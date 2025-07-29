import os
import check
from file import enroll_file

def enroll_course():#function to enroll a student in a course
    if not os.path.exists(enroll_file):#check if file exists
        with open(enroll_file, "w") as file:
            pass

    os.system('cls' if os.name == 'nt' else 'clear')#clear screen
    print("📖 ENROLL STUDENT IN COURSE\n")

    while True:
        student_id = input("🔹 Student Id (8 digits) or 'B' to go back : ")#asking user for student id
        if student_id.upper() == 'B':#if user enter 'B' then return to main menu
            return
        if not check.student_exists(student_id):#check if student id exists
            print("❌ ERROR: Student Id doesn't exist.\n")
            continue
        if not student_id.isdigit():#check if student id is in numbers
            print("❌ ERROR! Student ID has to be in numbers.\n")
            continue
        if len(str(student_id)) != 8:#check if student id is 8 digits
            print("❌ ERROR: Student Id has to be exactly 8 digits.\n")
            continue

        course_id = input("🔹 Course Id or 'B' to go back : ")#asking user for course id
        if course_id.upper() == 'B':#if user enter 'B' then return to main menu
            return
        if not check.course_exists(course_id):#check if course id exists
            print("❌ ERROR: Course Id does not exist.\n")
            continue
        if check.course_full(course_id):#check if course is full
            print("❌ ERROR: The course is full.\n")
            continue
        if check.student_enroll_exists(student_id, course_id):#check if student is already enrolled in the course
            print("❌ ERROR: Student has already enrolled in this course.\n")
            continue
        break

    seats_left = check.decrement_seat_count(course_id)#decrementing the seat count
    if seats_left is None or seats_left < 0:#if seats left is less than 0 then print this message
        print("❌ ERROR: Course is full.\n")
        return
    
    with open(enroll_file, "a") as file:
        file.write(f"{student_id},{course_id}\n")#storing the data user enter to the enroll file
    print(f"✅ Enrollment successful. Seats left: {seats_left}\n")
