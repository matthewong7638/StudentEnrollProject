import os
from file import course_file

def delete_course():#delete course function
    print("📑 DELETE COURSE\n")
    while True:
        course_id = input("🔹 Course ID to delete or 'B' to go back : ").strip()#asking user for course id to delete
        if course_id.upper() == 'B':#if user enter 'B' then return to main menu
            return

        if not os.path.exists(course_file):#check if file exists
            print("❌ ERROR: Course file does not exist.\n")
            return

        with open(course_file, 'r') as file:#open file in read mode
            lines = file.readlines()#reading the lines in the file

        with open(course_file, 'w') as file:#open file in write mode
            course_found = False#initializing course found to False
            for line in lines:
                if line.strip().split(',')[0] != course_id:#splitting the line and checking if course id exists
                    file.write(line)#writing the line to the file
                else:
                    course_found = True#setting course found to True

        if course_found:
            print(f"✅ Course with ID {course_id} has been deleted.\n")#if course found then print this message
        else:
            print(f"❌ ERROR: Course with ID {course_id} not found.\n")#if course not found then print this message