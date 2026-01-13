#import math

people = int(input("Enter number of people: "))
pizza_type = input(
    "Enter pizza type (Sapa Size, Small Money, Big Boys, Odogwu): "
).lower()

match pizza_type:
    case "sapa size":
        slices_per_box = 4
        price_per_box = 2000

    case "small money":
        slices_per_box = 6
        price_per_box = 2400

    case "big boys":
        slices_per_box = 8
        price_per_box = 3000

    case "odogwu":
        slices_per_box = 12
        price_per_box = 4200

    case _:
        print("Invalid pizza type!")
        exit()

# Calculations
#boxes = math.ceil(people / slices_per_box)
boxes = (people + slices_per_box - 1) // slices_per_box
total_slices = boxes * slices_per_box
leftover = total_slices - people
total_price = boxes * price_per_box

# Output
print("\nNumber of boxes of pizza to buy =", boxes)
print("Number of leftover slices =", leftover)
print("Total price =", total_price)

