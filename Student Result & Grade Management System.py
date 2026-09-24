print("------------------- WELCOME TO SANDIP UNIVERSITY -------------------")

while True:

    print("\n========= STUDENT RESULT SYSTEM =========")
    print("1. Enter Student Details")
    print("2. Exit")
    print("3. Future Feature")

    choice = int(input("Enter your choice :- "))

    # Invalid menu choice
    if choice < 1 or choice > 4:
        print("Invalid choice! Please enter 1 to 4.")
        continue

    # Exit
    if choice == 2:
        print("\nThank you for using Student Result System!")
        break

    # Future feature
    if choice == 3:
        print("\nThis feature will be added in the future.")
        pass
        continue

    # Student Details
    if choice == 1:

        Student_Name = input("Enter Student Name :- ")
        Roll_No = input("Enter Roll No :- ")
        Age = int(input("Enter your Age :- "))

        print("\n-------- Enter Student Marks of All Subjects --------")

        Subjects = ["Python", "Maths", "DBMS", "OS", "English"]

        total = 0

        for i in range(5):

            marks = int(input(f"Enter {Subjects[i]} Marks :- "))

            # Validate marks
            while marks < 0 or marks > 100:
                print("Invalid Marks! Please enter marks between 0 and 100.")
                marks = int(input(f"Enter {Subjects[i]} Marks :- "))

            total += marks

        # Calculate percentage
        percentage = (total / 500) * 100

        print("\n================ RESULT ================")

        print(f"Name       : {Student_Name}")
        print(f"Roll No    : {Roll_No}")
        print(f"Age        : {Age}")
        print(f"Total      : {total}/500")
        print(f"Percentage : {percentage:.2f}%")

        # Grade
        if percentage < 50:
            grade = "C"
        elif percentage < 80:
            grade = "B"
        else:
            grade = "A"

        print(f"Grade      : {grade}")

        # Pass / Fail
        if percentage >= 40:
            print("Result     : PASS")
        else:
            print("Result     : FAIL")

        print("========================================")
