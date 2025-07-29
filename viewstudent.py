import os
from file import student_file
import pandas as pd

def view_student():#function to view students
    os.system("cls" if os.name == "nt" else "clear")#clear screen
    print("➡️ VIEW STUDENTS\n")

    if not os.path.exists(student_file) or os.stat(student_file).st_size == 0:#check if file exists
        print("❌ No students available.\n")
        input("Press Enter to continue. . .\n")
        return
    
    df = pd.read_csv(student_file, names=["Student ID", "Student Name", "Student Contact"], dtype={"Student ID": str, "Student Name": str, "Student Contact": str}, index_col=False)#reading the student file

    if df.empty:#if file is empty then print this message
        print("❌ No students available.\n")
        input("Press Enter to continue. . .\n")
        return
    
    print(f"{'Student ID':<15} {'Student Name':<25} {'Student Contact':<20}")#printing the column names
    print("="*60)#printing '=' 60 times for cleaner table
    for index, row in df.iterrows():#iterating through the file
        print(f"{row['Student ID']:<15} {row['Student Name']:<25} {row['Student Contact']:<20}")#printing the data in the file

    print()
    input("Press Enter to continue...\n")#prompting user to press enter to continue to let user view the data