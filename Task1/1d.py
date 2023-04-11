# 1d. Create a program that calculates the lenght of hypotenuse of a right-angled
# triangle. The other 2 lengths are taken as inputs from the user
import math

# c^2 = a^2 + b^2 
print('Input the two length of a triangle')
while True:
    try:
        length_a = float(input('First length: '))
        length_b = float(input('Second length: '))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

print('The hypotenuse is = ', math.sqrt(pow(length_a, 2) + pow(length_b, 2)))
