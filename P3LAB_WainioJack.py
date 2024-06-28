
amount = float(input("Enter amount of money as a float: "))
    
    
cents = int(amount * 100)
    
    
dollars = cents // 100
cents %= 100
    
quarters = cents // 25
cents %= 25
    
dimes = cents // 10
cents %= 10
    
nickels = cents // 5
pennies = cents % 5
    
if dollars > 0:
        print(f"{dollars} {'dollar' if dollars == 1 else 'dollars'}")
    
if quarters > 0:
        print(f"{quarters} {'quarter' if quarters == 1 else 'quarters'}")
    
if dimes > 0:
        print(f"{dimes} {'dime' if dimes == 1 else 'dimes'}")
    
if nickels > 0:
        print(f"{nickels} {'nickel' if nickels == 1 else 'nickels'}")
    
if pennies > 0:
        print(f"{pennies} {'penny' if pennies == 1 else 'pennies'}")


