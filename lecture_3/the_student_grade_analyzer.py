# Student Grade Analyzer Program

# 1. Initialize the main data structure: a list to store student dictionaries.
students = []


def add_student():
    """Add a new student to the system."""
    name = input("Enter student name: ").strip()
    # Check if student already exists (case-insensitive comparison)
    if any(student['name'].lower() == name.lower() for student in students):
        print(f"Student '{name}' already exists.")
        return
    # Create a new student dictionary with an empty grades list and add it to the students list.
    new_student = {'name': name, 'grades': []}
    students.append(new_student)
    print(f"Student '{name}' added successfully.")


def add_grades():
    """Add one or more grades for an existing student."""
    name = input("Enter student name: ").strip()
    # Find the student by name (case-insensitive)
    student = None
    for s in students:
        if s['name'].lower() == name.lower():
            student = s
            break
    # If student not found, inform the user.
    if student is None:
        print(f"Student '{name}' not found.")
        return
    # Prompt for grades until user enters 'done'
    while True:
        grade_input = input("Enter a grade (or 'done' to finish): ").strip()
        if grade_input.lower() == 'done':
            break
        try:
            # Convert input to integer and validate range [0, 100]
            grade = int(grade_input)
            if 0 <= grade <= 100:
                student['grades'].append(grade)
                print(f"Grade {grade} added for {student['name']}.")
            else:
                print("Invalid grade. Please enter a number between 0 and 100.")
        except ValueError:
            # Handle non-integer input
            print("Invalid input. Please enter a number.")


def calculate_average(grades):
    """Calculate and return the average of a list of grades.
    Returns None if the list is empty to avoid ZeroDivisionError."""
    if len(grades) == 0:
        return None
    return sum(grades) / len(grades)


def show_report():
    """Generate and display a report for all students."""
    if len(students) == 0:
        print("No students have been added yet.")
        return
    # Lists to store averages for summary statistics
    averages = []
    # Iterate through each student
    for student in students:
        avg = calculate_average(student['grades'])
        if avg is not None:
            # Print individual student average
            print(f"{student['name']}'s average grade is {avg:.1f}.")
            averages.append(avg)
        else:
            # Handle case where student has no grades
            print(f"{student['name']}'s average grade is N/A.")
    # If no valid averages were calculated, print a message.
    if len(averages) == 0:
        print("No grades have been added for any student.")
        return
    # Calculate and print summary statistics
    max_avg = max(averages)
    min_avg = min(averages)
    overall_avg = sum(averages) / len(averages)
    print("-" * 20)
    print(f"Max Average: {max_avg:.1f}")
    print(f"Min Average: {min_avg:.1f}")
    print(f"Overall Average: {overall_avg:.1f}")


def find_top_performer():
    """Find and display the student with the highest average grade."""
    # Filter students who have at least one grade
    students_with_grades = [s for s in students if len(s['grades']) > 0]
    # If no students have grades, inform the user.
    if len(students_with_grades) == 0:
        print("No top student. No students have been added or no grades have been added.")
        return
    # Use max() with a lambda function to find the student with the highest average.
    # The lambda calculates the average for each student's grades.
    top_student = max(students_with_grades,
                      key=lambda s: calculate_average(s['grades']))
    top_avg = calculate_average(top_student['grades'])
    print(
        f"The student with the highest average is {top_student['name']} with a grade of {top_avg:.1f}.")


def main():
    """Main program loop that displays the menu and handles user choices."""
    while True:
        # Display the menu
        print("\n--- Student Grade Analyzer ---")
        print("1. Add a new student")
        print("2. Add grades for a student")
        print("3. Generate a full report")
        print("4. Find the top student")
        print("5. Exit program")
        # Get user choice with error handling
        try:
            choice = int(input("Enter your choice: "))
            # Process the choice
            if choice == 1:
                add_student()
            elif choice == 2:
                add_grades()
            elif choice == 3:
                show_report()
            elif choice == 4:
                find_top_performer()
            elif choice == 5:
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please select a number from 1 to 5.")
        except ValueError:
            # Handle non-integer input for menu choice
            print("Invalid input. Please enter a number.")


# Entry point of the program
if __name__ == "__main__":
    main()
