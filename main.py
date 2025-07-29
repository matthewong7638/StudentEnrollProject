import addstudent
import addcourse
import enrollcourse
import dropcourse
import viewstudent
import viewcourse
import deletestudent
import deletecourse
#import function from other files

def main():#main registration menu
    while True:
        print("🎓 COURSE REGISTRATION SYSTEM 🎓")
        print("=========================================")
        print("[1] ➕  Add Student")
        print("[2] ➕  Add Course")
        print("[3] ✏️   Enroll Course")
        print("[4] 📌  Drop Course")
        print("[5] 👀  View Student")
        print("[6] 👀  View Course")
        print("[7] ❌  Delete Student")
        print("[8] ❌  Delete Course")
        print("[9] 🏃  Exit")

        choice = input("🔹Enter choice : ").strip()#choices statement
        if choice == '1':
            addstudent.add_student()
        elif choice == '2':
            addcourse.add_course()
        elif choice == '3':
            enrollcourse.enroll_course()
        elif choice == '4':
            dropcourse.drop_course()
        elif choice == '5':
            viewstudent.view_student()
        elif choice == '6':
            viewcourse.view_course()
        elif choice == '7':
            deletestudent.delete_student()
        elif choice == '8':
            deletecourse.delete_course()
        elif choice == '9':
            print("👋 Exiting... Thank You!\n")
            break
        else:
            print("❌ Invalid input. Please try again.\n")
            continue # continue the loop

if __name__ == "__main__":
    main()#making sure only this file is to be run