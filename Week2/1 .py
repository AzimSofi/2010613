# 1. Create a program that asks the user to provide several numbers
# and output the total and the average of the numbers.

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
