# 1. Create a program that asks the user to provide several numbers
# and output the total and the average of the numbers.

def average(total, size):
    return total/size


print("How many numbers would you like: ")
inputSize = int(input())

cumulative = 0
for i in range(0, inputSize):
    print("User input: ")
    usersInput = float(input())
    cumulative = usersInput + cumulative

print("Your input average is ", average(cumulative, inputSize))
