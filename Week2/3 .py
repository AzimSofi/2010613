# 3. Create a program that asks the user to provide 2 numbers 
# and output the GCD (Greatest Common Divisor) and LCM (Lowest Common Multiple) 
# of both numbers.

def LCM(num1, num2):
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
    return int(num1*num2/LCM(num1, num2))


print("Input 2 numbers to find the GCD (Greatest Common Divisor) and LCM (Lowest Common Multiple) of the two number.")
print("First input")
inputOne = int(input())

print("Second input")
inputTwo = int(input())

print("GCD: ", GCD(inputOne, inputTwo))
print("LCM: ", LCM(inputOne, inputTwo))
