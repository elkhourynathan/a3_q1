from crud import get_all_students, add_student, update_student_email, delete_student

def main():
    get_all_students()
    input("Press any letter to continue ")
    add_student("Test", "Test", "test@gmail.com", "2021-09-01")
    get_all_students()
    input("Press any letter to continue ")
    update_student_email(1, "random@random.com")
    get_all_students()
    input("Press any letter to continue ")
    delete_student(1)
    get_all_students()

if __name__ == "__main__":
    main()