# 1. The Big Result
#
# Write an add_mult function that requires three parameters / arguments
# Returns the result that is the sum of the 2 smallest arguments multiplied by the largest argument value.
# PS Assume that numeric parameters will always be passed to the function, no need to check types
# Various solutions are possible (you are allowed to use other data structures inside function such as list).
#
# Example add_mult (2,5,4) -> will return (2 + 4) * 5 = 30


def add_mult(a, b, c):
    numbers = [a, b, c]
    max_num = max(numbers)  #finding largest number
    numbers.remove(max_num)    #removing largest number
    return sum(numbers) * max_num


print(add_mult(2, 5, 4))
