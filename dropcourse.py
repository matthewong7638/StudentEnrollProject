import os
import check
from file import enroll_file, course_file

def drop_course():#drop course function
    print("⬇️ DROP STUDENT FROM COURSE\n")

    while True:
        student_id = input("🔹 Student ID or 'B' to go back : ")#asking user for student id
        if student_id.upper() == 'B':#if user enter 'B' then return to main menu
            return
        if not check.student_exists(student_id):#check if student id exists
            print("❌ ERROR: Student ID does not exist\n")
            continue

        course_id = input("🔹 Course Id or 'B' to go back : ")#asking user for course id to drop
        if course_id.upper() == 'B':#if user enter 'B' then return to main menu
            return
        if not check.course_exists(course_id):#check if course id exists
            print("❌ ERROR: Course ID does not exist.\n")
            continue
        if not check.student_enroll_exists(student_id, course_id):#check if student enroll in the course
            print("❌ ERROR: Student has not enrolled in this course.\n")
            continue
        break
    
    with open(enroll_file, "r") as file:
        lines = file.readlines()#reading the lines in the file
    with open(enroll_file, "w") as file:
        for line in lines:#looping through the lines
            if line.strip() != f"{student_id},{course_id}":#checking if student id and course id exists
                file.write(line)#writing the line to the file

    check.increment_seat_count(course_id) #increment seat count when student drops

    print(f"✅ Student {student_id} has been dropped from course {course_id}.\n")
