# 2. Create a program that prints all numbers from 0 to 50 
# and tell the user if the number is odd or even.

for i in range(0, 50 + 1):
    if (i%2 == 0):
        print(i, "is even.")
    else:
        print(i, "is odd.")
