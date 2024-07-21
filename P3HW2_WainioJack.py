#Jack Wainio
#6-28-2024
#Employee Compensation Calculator

#Prompt employee information
employee_name = input("Enter name of employee: ")
hours_worked = float(input("Enter number of hours the employee worked this week: "))
pay_rate = float(input("Enter employee's pay rate per hour: "))
    
    # Calculate overtime pay if any
if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_hours = 40
else:
        overtime_hours = 0
        regular_hours = hours_worked
    
    # Calculate gross pay
regular_pay = regular_hours * pay_rate
overtime_pay = overtime_hours * (pay_rate * 1.5)  # Overtime rate is 1.5 times regular pay rate
gross_pay = regular_pay + overtime_pay
    
    # Display results
print("\nPayroll Summary:")
print("Employee Name   Hours Worked   Pay Rate   Overtime Hours   Overtime Pay   Regular Pay   Gross Pay")
print("-------------------------------------------------------------------------------------------------")
print(f"{employee_name:<15}{hours_worked:<15.2f}{pay_rate:<15.2f}{overtime_hours:<15.2f}{overtime_pay:<15.2f}{regular_pay:<15.2f}{gross_pay:<15.2f}")

      
