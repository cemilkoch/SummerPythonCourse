# Challenge
# Ask the user to enter number of sides(Up to 10)
# Read the number of sides and determine shape

sides = int(input("Enter the number of sides: "))

if sides == 3:
    print("Triangle")
elif sides == 4:
    print("Square")
elif sides == 5:
    print("Pentagon")
elif sides == 6:
    print("Hexagon")
elif sides ==7:
    print("Heptagon")
elif sides == 8:
    print("Octagon")
elif sides == 9:
    print("Nonagon")
elif sides == 10:
    print("Decagon")
else:
    print("Invalid side number...")