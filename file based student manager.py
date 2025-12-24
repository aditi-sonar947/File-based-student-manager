FILE_NAME ="students.txt"

def add_student():
    name = input("Enter student name: ")
    marks = input("Enter marks: ")

    with open(FILE_NAME, "a") as file:
        file.write(name + "," + marks +"\n")

    print("Students added successfully")

def view_students():
    try:
        with open(FILE_NAME,"r") as file:
            lines = file.readlines()

            if not lines:
                print("No students found.")
                return
            print("\n---Student list---")
            for i in range(len(lines)):
                name, marks = lines[i].strip().split(",")
                print(i+1 , name,"-",marks)

    except FileNotFoundError:
        print("No data file found. ")

while True:
    print("\n--- STUDENT MANAGER ---")
    print("1. Add student")
    print("2. View Student")
    print("3. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        add_student()
    elif choice =="2":
        view_students()
    elif choice == "3":
        print("Goodbye ")
        break
    else:
        print("Invalid Choice")