# 1. FizzBuzz
#
# Print a string 1,2,3,4, Fizz, 6, Buzz, 8, ..... 34, FizzBuzz, 36, .... to 97, Buzz, 99, Fizz So if number divided
# by 5 then Fizz If divided by 7 then Buzz, If divided by 5 AND 7 then FizzBuzz otherwise the same number Note: such
# a task became popular as the first task to ask to determine whether a person knows about programming at all smile


for a in range(1, 101):
    if a % 5 == 0 and a % 7 == 0:
        print("FizzBuzz", end=",")
    elif a % 5 == 0:
        print("Fizz", end=",")
    elif a % 7 == 0:
        print("Buzz", end=",")
    else:
        print(a, end=",")


#  2. Christmas tree
#
# Enter the height of the tree
# Print the tree: Ex. height == 3
# The printout would be:
#
#   *
#
#  ***
#
# *****
#
# Note: remember that several symbols can be printed at once, for example: print ("" * 10 + "*" * 6)

height = int(input("How many lines you want your Christmas tree? "))
for i in range(height):
    print(" " * (height - i - 1) + "*" * (2 * i + 1))

# 3. Primes Check if entered positive number is a prime number.
#
#  A prime number is a number that divides without remainder only by itself and 1.
#
# Hint: what numbers do we have to check?

num = int(input("Enter your number: "))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

# if less than or equal to 1, it is not prime
else:
    print(num, "is not a prime number")