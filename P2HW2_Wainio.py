#Jack Wainio
#6/20/24
#P2HW2
#Grade Calculator
grades_list = []
for i in range(1, 7):
    # Ask the user to enter a grade for Module i
    grade = float(input("Enter grade for Module " + str(i) + ": "))
    # Append the grade to the list
    grades_list.append(grade)
    lowest_grade = min(grades_list)
highest_grade = max(grades_list)
sum_of_grades = sum(grades_list)
average_grade = sum_of_grades / len(grades_list)
print("The lowest grade is:\t", lowest_grade)
print("The highest grade is:\t", highest_grade)
print("Sum of grades is:\t", sum_of_grades)
print("The grades' average is:\t {:.2f}".format(average_grade))
