# 2. Xmas Bonus

# The company has promised a Christmas bonus in the amount of 15% of the monthly salary for EVERY year of service over 2 years.

# Task. Ask the user for the amount of the monthly salary and the number of years worked.
worked_years = float(input("How many years you've worked? "))
years_needed = int(2)
# Calculate the bonus.
if worked_years <= years_needed:
    print("Not enough years, no bonus")   
else:
    salary = float(input("What's your salary? "))
    bonus = (worked_years - years_needed) * 0.15 * salary
    print(f"Your bonus is {round(bonus, 2)}")

# Example1: 5 years of experience, 1000 Euro salary, the bonus will be 450 Euro.

# Example2: 1.5 years of experience, 1500 Euro salary, no bonus(0).