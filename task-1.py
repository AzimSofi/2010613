# 1a. Create a program that asks the user to provide several numbers
# and output the total and the average of the numbers.

# region Task 1a

def average(total, size):
    if size == 0:
        return 0
    return total/size

while True:
    try:
        input_size = int(input("How many numbers would you like: "))
        if input_size < 0:
            print("Invalid input. Please enter a positive integer:")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter an integer:")
        
cumulative = float()
for i in range(0, input_size):
    
    while True:
        try:
            users_input = float(input("User input: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number:")
    cumulative += users_input

print("Your input total is ", cumulative)
print("Your input average is ", average(cumulative, input_size))
# endregion

# 1b. Create a program that prints all numbers from 0 to 50 
# and tell the user if the number is odd or even.

# region Task 1b
for i in range(0, 50 + 1):
    if (i%2 == 0):
        print(i, "is even.")
    else:
        print(i, "is odd.")
# endregion


# 1c. Create a program that asks the user to provide 2 numbers 
# and output the GCD (Greatest Common Divisor) and LCM (Lowest Common Multiple) 
# of both numbers.

# region Task 1c
def LCM(num1, num2):
    # Check for zero input
    if num1 == 0  and num2 == 0:
        return "undefined"
    elif num1 ==0 or num2 == 0:
        return 0
    
    # To keep track of each multiplicative
    oldnum1 = num1
    oldnum2 = num2
    
    # LCM of two numbers should be equal to each other
    # While theyre not equal, iteratively check their multiplacitive
    while (num1 != num2):
        while (num2 > num1):
            num1 += oldnum1
        while (num1 > num2):
            num2 += oldnum2

    return num1 # Or return num2

# GCD can be define by LCM, so just reuse the LCM method
def GCD(num1, num2):
    if num1 == 0 and num2 == 0:
        return "undefined"
    elif num1 == 0:
        return num2
    elif num2 == 0:
        return num1
    else:
        return int(num1*num2/LCM(num1, num2))


print("Input 2 numbers to find the GCD (Greatest Common Divisor) and LCM (Lowest Common Multiple) of the two numbers.")
while True:
    try:
        input_one = int(input("First input: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

while True:
    try:
        input_two = int(input("Second input: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

print("GCD: ", GCD(input_one, input_two))
print("LCM: ", LCM(input_one, input_two))
# endregion

# 1d. Create a program that calculates the lenght of hypotenuse of a right-angled
# triangle. The other 2 lengths are taken as inputs from the user

# region Task 1d
# c^2 = a^2 + b^2 
import math

print('Input the two length of a triangle')
while True:
    try:
        length_a = float(input('First length: '))
        length_b = float(input('Second length: '))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

print('The hypotenuse is = ', math.sqrt(pow(length_a, 2) + pow(length_b, 2)))
# endregion
