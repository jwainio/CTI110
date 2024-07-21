#Jack Wainio
#7/7/24
#Pay Calculator

def calculate_pay(pay_rate, hours_worked):
    regular_pay = 0
    overtime_pay = 0

    if hours_worked <= 40:
        regular_pay = hours_worked * pay_rate
    else:
        regular_pay = 40 * pay_rate
        overtime_pay = (hours_worked - 40) * (1.5 * pay_rate)

    return regular_pay, overtime_pay

def main():
    employees = []
    while True:
        employee_name = input("Enter employee name (or 'Done' to terminate): ")
        
        if employee_name.lower() == 'done':
            break
        
        pay_rate = float(input("Enter pay rate per hour: "))
        hours_worked = float(input("Enter hours worked: "))
        
        regular_pay, overtime_pay = calculate_pay(pay_rate, hours_worked)
        
        employees.append({
            'name': employee_name,
            'regular_pay': regular_pay,
            'overtime_pay': overtime_pay,
            'total_pay': regular_pay + overtime_pay
        })
    
    if employees:
        print("\nResults:")
        overtime_total = 0
        regular_pay_total = 0
        gross_pay_total = 0

        for emp in employees:
            overtime_total += emp['overtime_pay']
            regular_pay_total += emp['regular_pay']
            gross_pay_total += emp['total_pay']

        num_employees = len(employees)

        print(f"Number of employees: {num_employees}")
        print(f"Total overtime pay: ${overtime_total:.2f}")
        print(f"Total regular pay: ${regular_pay_total:.2f}")
        print(f"Gross pay total: ${gross_pay_total:.2f}")
    else:
        print("No employees entered.")

if __name__ == "__main__":
    main()
