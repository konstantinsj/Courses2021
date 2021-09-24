# 3. Exercise - Temperature Conversion

# Write a program that asks user for temperature in Celsius and prints out this same temperature in Farenheit
# formula is: farenheit = 32+celsius*(9/5)
# PS Remember about data type conversion, also consider precision

#asking user input
celsius = float(input("Please input degrees in Celsius "))

# precision is 2 digits
prec = 2

#convert celsius to farenheit 
farenheit = 32+celsius*(9/5)
print(f"{celsius} degrees in Celsius is {round(farenheit, prec)} degrees in Farenheit")
