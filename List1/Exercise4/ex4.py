#Student's grade on test, student's grade on assignments and student's attendance

grade = float(input("Student's grade on test: "))
assignments = float(input("Student's grade on assignments: "))
attendance = float(input("Student's grade on attendance: "))

average = (0.3 * assignments) + (0.7 * grade)

if (average >= 6.0 and attendance >= 75.0):
    print("Student approved")
elif (average < 6.0 and average >= 4.0 and attendance >= 75.0):
    print("Student must make recovery")
elif (average < 4.0 or attendance < 75.0):
    print("Student reproved")


