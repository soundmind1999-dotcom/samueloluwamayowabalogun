distance = float(input("Enter the driving distance: "))

miles_per_gallon = float(input("Enter miles per gallon: "))

price_per_gallon = float(input("Enter price per gallon: "))

cost = (distance / miles_per_gallon) * price_per_gallon

print(f"The cost of driving is ${cost:.2f}")
