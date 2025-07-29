import os
from file import student_file, course_file, enroll_file

def student_exists(student_id):#function to check if student exists
    if not os.path.exists(student_file):#check if file exists
        return False
    with open(student_file, "r") as file:#open file in read mode
        for line in file:
            if line.startswith(student_id + ','):#check if student id exists
                return True#if student id exists then return True
    return False

def course_exists(course_id):#function to check if course exists
    if not os.path.exists(course_file):#check if file exists
        return False
    with open(course_file, "r") as file:#open file in read mode
        for line in file:
            if line.startswith(course_id + ','):#check if course id exists
                return True#if course id exists then return True
    return False

def student_enroll_exists(student_id, course_id):#function to check if student is enrolled
    if not os.path.exists(enroll_file):#check if file exists
        return False
    with open(enroll_file, "r") as file:#open file in read mode
        for line in file:
            if line.startswith(student_id + "," + course_id):#check if student is enrolled
                return True#if student is enrolled then return True
    return False

def course_full(course_id):#function to check if course is full
    if not os.path.exists(course_file):#check if file exists
        return False
    
    max_seats = None#initialize max_seats to None
    with open(course_file, "r") as file:#open file in read mode
        for line in file:
            parts = line.strip().split(",")#split the line by ','
            if len(parts) < 3:
                continue#skip if line has less than 3 values
            if parts[0] == course_id:#check if course id matches
                max_seats = int(parts[2])#set max_seats to available seats
                break
    
    if max_seats is None:#if course id not found return False
        return False
    if max_seats <= 0:
        return True # Fix: Correct comparison

def decrement_seat_count(course_id):#function to decrement available seat count
    course_lines = []#initialize list to store updated data
    max_seats = None
    
    with open(course_file, "r") as file:#open file in read mode
        for line in file:
            parts = line.strip().split(",")#split the line by ','
            if parts[0] == course_id:#check if course id matches
                max_seats = int(parts[2])#set max_seats
                if max_seats > 0:#check if seats are available
                    parts[2] = str(max(0, max_seats - 1))#decrement seat count ensuring it doesn't go negative
                line = ",".join(parts)#join updated parts back to string
            course_lines.append(line)#append line to list
    
    with open(course_file, "w") as file:#open file in write mode
        for line in course_lines:
            file.write(line + "\n")#write updated data back to file
    
    return int(parts[2]) if max_seats is not None else None#return updated seat count

def increment_seat_count(course_id):#function to increment available seat count
    course_lines = []#initialize list to store updated data
    with open(course_file, "r") as file:#open file in read mode
        for line in file:
            parts = line.strip().split(",")#split the line by ','
            if parts[0] == course_id:#check if course id matches
                parts[2] = str(int(parts[2]) + 1)#increment seat count
                line = ",".join(parts)#join updated parts back to string
            course_lines.append(line)#append line to list
    
    with open(course_file, "w") as file:#open file in write mode
        for line in course_lines:
            file.write(line + "\n")#write updated data back to file