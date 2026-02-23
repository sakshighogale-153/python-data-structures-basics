# Create a dictionary of student marks
student_marks = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78
}

# Ask the user to input a student's name
name = input("Enter the student's name: ")

# Retrieve and display the marks
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found.")
