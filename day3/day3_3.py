# 3. Ordered output.

# Ask the user to enter 3 numbers, output them in ascending order.

num1 = -9
num2 = 15
num3 = 0

# output them in ascending order.

if num1 < num2:
    tmp = 0
    tmp = num1
    num1 = num2
    num2 = tmp
if num1 < num3:
    tmp = 0
    tmp = num1
    num1 = num3
    num3 = tmp
if num2 < num3:
    tmp = 0
    tmp = num2
    num2 = num3
    num3 = tmp
print(num3, num2, num1)

# Note: for now, we solve this task only with if, elif, else actions.
# There is also a solution using sorting and list structure, which we have not yet seen.
