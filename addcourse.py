import os
import check
from file import course_file

def add_course():#add course function
    if not os.path.exists(course_file):#check if file exists
        with open(course_file, "w") as file:   
            pass
        
    os.system('cls' if os.name == 'nt' else 'clear')#clear screen
    print("➕📚 ADD COURSE\n")

    while True:
        course_id = input("🔹 Course Id or 'B' to go back : ")#promting user to enter course id
        if course_id.upper() == 'B':#if user enter 'B' then return to main menu
            return
        if not course_id.isdigit():#check if course id is in numbers
            print("❌ ERROR: Course ID has to be in numbers.\n")
            continue
        if check.course_exists(course_id):#check if course id exists
            print("❌ ERROR: Course Id already exists.\n")
            continue
      
        course_name = input("🔹 Course Name or 'B' to go back : ")#asking user to enter course name
        if course_name.upper() == 'B':#if user enter 'B' then return to main menu
            return
        if course_name.isdigit():#check if course name is in numbers
            print("❌ ERROR: Course Name invalid.\n")
            continue
        if not all(x.isalpha() or x.isspace() or x in '()' for x in course_name):#check if course name is in alphabets
            print("❌ ERROR: Course Name invalid.\n")
            continue
        
        max_seat = input("🔹 Max seats (Must be > 0) or 'B' to go back : ")#asking user to enter the max seat for the course
        if max_seat.upper() == 'B':#if user enter 'B' then return to main menu
            return
        if not max_seat.isdigit():#check if max seat is in numbers
            print("❌ ERROR: Max Seat has to be in numbers\n")
            continue
        if not int(max_seat) > 0:#check if max seat is greater than 0
            print("❌ ERROR: Seats has to be greater than 0.\n")
            continue
        break
    with open(course_file, "a") as file:
        file.write(f"{course_id},{course_name},{max_seat}\n")#storing the data user enter to the course file
            
    print("✅ Course added successfully.\n")