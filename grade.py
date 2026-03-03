"""
Gradebook App
- list creation
- indexes
- basic list options
- tracks student grades
"""

student_names = []
student_grades = []


def create_course() -> str:
    """Ask user for course name and return it."""
    return input("Enter course name: ").strip().title()


def add_student():
    """Add a single student with a grade."""
    name = input("Enter student name: ").strip().title()
    grade = int(input("Enter student percentage: ").strip())

    student_names.append(name)  # Append will add to the list
    student_grades.append(grade)


def update_grade():
    """Update the grade for an existing student."""
    name = input("Enter student to update: ").strip().title()

    if (
        name in student_names
    ):  # This is how you loop through a list and search for an item
        index = student_names.index(name)  # Find out the index number of that student
        new_grade = int(input(f"Enter new grade for {name}: ").strip())
        student_grades[index] = new_grade
    else:
        print("No student by that name")


def remove_student():
    """Remove a student and their grade."""
    # What student to remove?
    name = input("Which student do you want to remove?").strip().title()

    # Check if student is in list

    # If in list, then remove student and their grade
    if name in student_names:  # Checks if names entered are in list
        index = student_names.index(name)  # Get the index of the name entered
        student_names.pop(index)  # Pops or removes student from index
        student_grades.pop(index)
        print("Student removed.")
    else:
        print("There are no students by that name.")


def show_roster():
    """Display all students and grades."""
    # Do something for no students in roster
    if not student_names:
        print("No students in course.")
        return
    # Loop through the list of students and show name and grade
    print("\nClass Roster")
    for index in range(len(student_names)):
        print(student_names[i], " - ", student_grades[i])


def show_statistics():
    """Display class statistics."""
    # If there are no students, tell user
    if not student_names:
        print("There are no studetns.")
        return

    # Calculate the average of the class
    average = sum(student_grades) / len(student_grades)
    # Output the average, highest score, lowest score
    print("\nClass Statistics:")
    print("Average: ", round(average, 2))
    print("Highest mark: ", max(student_grades))
    print("Lowest mark: ", min(student_grades))


def main():
    """
    Main program loop - runs all other functions
    """
    # Create a new course
    course = create_course()
    # Welcome user to the course
    print(f"\nWelcome to {course}!")
    # Show options for user to choose
    while True:
        print("\n1 - Add Student")
        print("2 - Update Grade")
        print("3 - Remove Student")
        print("4 - Show Rosster")
        print("5 - Show Statistics")
        print("0 - Exit")

        choice = input("Choose an option")
        # Based on choice, run feature
        # Features:
        # Add student
        if choice == "1":
            add_student()
        # Update grade
        elif choice == "2":
            update_grade()
        # Remove student
        elif choice == "3":
            remove_student()
        # Show roster
        elif choice == "4":
            show_roster()
        # Show stats
        elif choice == "5":
            show_statistics()
        # Exit
        elif choice == "0":
            break
        else:
            print("That is not one of the options!")


if __name__ == "__main__":
    main()
