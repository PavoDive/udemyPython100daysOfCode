bill = float(input("What was the total bill? $"))
tip = int(input("What would you like to tip: 10, 12 or 15? "))
people = int(input("How many people are splitting the bill? "))

total_bill = bill * (1 + tip / 100)
individual_bill = total_bill / people

print(f"Each person should pay: ${'{:.2f}'.format(individual_bill)}")
