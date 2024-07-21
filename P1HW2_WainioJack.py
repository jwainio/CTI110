# Jack Wainio
 # June 20th
 # P2HW1
 # A Travel Budget

budget = int(input("Whats your budget:"))

travel_destination = input("Wheres your destination:")

gas_money = int(input("How much will you spend on gas:"))

accomadations = int(input("How much will you spend on accomadations:"))

food = int(input("How much will you spend on food:"))

expenses = gas_money + accomadations + food

remainder =  budget - expenses

print("---------------Travel Expense---------------")
print(f"{'Location:' : <20}", f"{ travel_destination : <20}")
print(f"{'Initial budget:' : <20}", f"${budget:.2f}")
print(f"{'Fuel:' : <20}", f"${gas_money:.2f}")
print(f"{'Accommodation:' : <20}", f"${accomadations:.2f}")
print(f"{'Food:' : <20}", f"${food:.2f}")

print("--------------------------------------------")
print(f"{'Remaining balance:' : <20}", f"{'$'+str(float(remainder)) : <20}")
