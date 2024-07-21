def display_multiplication_table(num):
    print(f"Multiplication table for {num}:")
    for i in range(1, 13):
        print(f"{num} x {i} = {num * i}")

def main():
    while True:
        user_input = input("Enter an integer:")
        
        try:
            num = int(user_input)
            if num < 0:
                print("Sorry, negative numbers are not accepted.")
            else:
                display_multiplication_table(num)
        except ValueError:
            print("Invalid input. Please enter an integer.")

        run_again = input("Do you want to run again? (yes/no): ").lower()
        if run_again != 'yes':
            print("Exiting program...")
            break

if __name__ == "__main__":
    main()
