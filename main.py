print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill ? $"))
percentage_tip = float(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100
people = int(input("How many people to split the bill? "))

bill_with_tip = total_bill + (total_bill * percentage_tip)
value_each_person = bill_with_tip / people
message = f"Each person should pay: ${value_each_person:.2f}"

print(message)
