import os
from file import course_file
import pandas as pd

def view_course():#function to view courses
    os.system("cls" if os.name == "nt" else "clear")#clear screen
    print("➡️ VIEW COURSES\n")

    if not os.path.exists(course_file) or os.stat(course_file).st_size == 0:#check if file exists
        print("❌ No courses available.\n")
        input("Press Enter to continue. . .\n")
        return
    
    df = pd.read_csv(course_file, names=["Course ID", "Course Name", "Seats Available"], dtype={"Course ID": str, "Course Name": str, "Seats Available": int}, index_col=False)#reading the course file

    if df.empty:#if file is empty then print this message
        print("❌ No courses available.\n")
        input("Press Enter to continue. . .\n")
        return
    
    print(f"{'Course ID':<15} {'Course Name':<25} {'Seats Available':<20}")#printing the column names
    print("="*60)#printing '=' 60 times for cleaner table
    for index, row in df.iterrows():#iterating through the file
        print(f"{row['Course ID']:<15} {row['Course Name']:<25} {row['Seats Available']:<20}")#printing the data in the file

    print()
    input("Press Enter to continue...\n")#prompting user to press enter to continue to let user view the data