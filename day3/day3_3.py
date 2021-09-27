# 3. Ordered output.

# Ask the user to enter 3 numbers, output them in ascending order.

num1 = float(input("Type your number 1: "))
num2 = float(input("Type your number 2: "))
num3 = float(input("Type your number 3: "))

# output them in ascending order.
#TODO this is ugly :)
if num1 < num2 and num1 < num3:
    if num2 < num3:
        print(num1,num2,num3)
    else:
        print(num1,num3,num2)
elif num2 < num3 and num2 < num3:
    if num3 < num1:
        print(num2,num3,num1)
    else:
        print(num2,num1,num3)
elif num3 < num1 and num3 < num2:
    if num2 < num1:
        print(num3,num2,num1)
    else:
        print(num3,num1,num2)


# Note: for now, we solve this task only with if, elif, else actions.

# There is also a solution using sorting and list structure, which we have not yet seen.

