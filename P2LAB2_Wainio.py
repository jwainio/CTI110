#Jack Wainio
#6/20/24
#P2Lab2
#Car dictionary
car_dict = {
    "Camaro":"18.21",
    "Prius":"52.36",
    "Model S":"110",
    "Silverado":"26",
    }
keys = car_dict.keys()
print(f"Keys in the dictionary: {list(keys)}")
user_input = input("Enter a vehicle to see its mpg:")
if user_input in car_dict:
    mpg = car_dict[user_input]
    print(f"MPG for {user_input}: {mpg}")
else:
    print(f"Vehicle '{user_input}' not found in the dictionary.")
miles = float(input("Enter the number of miles to drive: "))
if user_input in car_dict:
    mpg = float(car_dict[user_input])
    gallons_needed = miles / mpg
    print(f"Gallons of gas needed: {gallons_needed:.2f}")
else:
    print("Cannot calculate gallons needed as vehicle was not found.")
