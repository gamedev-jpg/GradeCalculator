"""System module."""
questions_on_assignment = float(input("Number of questions on the assignment: "))
questions_answered_correctly = float(input("Number of questions answered correctly: "))

grade_percent_in_decimal = questions_answered_correctly / questions_on_assignment
grade_percent = grade_percent_in_decimal * 100

if grade_percent >= 90:
    print("Your grade is an A")
elif grade_percent >= 80 and grade_percent < 90:
    print("Your grade is a B")
elif grade_percent >= 70 and grade_percent < 80:
    print("Your grade is a C")
elif grade_percent >= 60 and grade_percent < 70:
    print("Your grade is a D")
elif grade_percent < 60:
    print("Your grade is an F")
