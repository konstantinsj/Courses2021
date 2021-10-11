# 1a. Average value
#
# Write a program that prompts the user to enter numbers (float).
# The program shows the average value of all entered numbers after each entry.

num_avg = []
num = ""

while True:

    num = input("Enter number (enter 'q' to quit): ")
    if num == 'q':
        break
    else:
        num_avg.append(float(num))
        average = sum(num_avg) / len(num_avg)
        print(f" Average for input numbers is {round(average,2)}")
        print(f" Input numbers are: {', '.join([str(elem) for elem in num_avg])}")
        print(f"BOTTOM 3 {sorted(num_avg)[:3]}")
        print(f"TOP 3 {sorted(num_avg)[-3:]}")


#
# PS. 1a can do without a list
#
# 1b. The program shows both the average value of the numbers and ALL the numbers entered
# PS Exit the program  by entering "q"
#
# 1c The program does not show all the numbers entered but only TOP3 and BOTTOM3 and of course still average.
