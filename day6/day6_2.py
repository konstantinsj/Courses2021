# 2. Cubes
#
# The user enters the beginning (integer) and end number.
# The output is the entered numbers and their cubes
# For example: inputs 2 and 5 (two inputs)
#
# Output

input_1 = int(input("Enter 1st number: "))
input_2 = int(input("Enter last number: "))

numbers_cubed = []
numbers = list(range(input_1, input_2+1))

for i in numbers:
    numbers_cubed.append(i * i * i)
for i, n in enumerate(numbers_cubed):
    print(f"{numbers[i]} cubed: {numbers_cubed[i]}")

print(f"All cubes: {numbers_cubed}")
#
# 2 cubed: 8
# 3 cubed: 27
# 4 cubed: 64
# 5 cubed: 125
#
# All cubes: [8,27,64,125]
#
# PS could theoretically do without a list, but with a list it will be more convenient
