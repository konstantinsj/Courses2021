# . Exercise - Age 100

# Write a program that asks for and saves a username
# Ask a question about the user's age, using the username in the question.
# Shows in how many years the user will be 100 years old smile
# BONUS: Let the program also show the year when the user will be 100 years old.
# It could use a variable with the current year.
# It would be even better to get the current year automatically
# then you will need two additional lines:
# import datetime # let's talk about imports separately
# currentYear = datetime.datetime.now (). year

#import
from datetime import date

# creating the date object of today's date
todays_date = date.today()
  
# asking user name
user_name = input("What is your name? ")

# asking user age
user_age = input(f"What is your age, {user_name}? ")

# years when user turns 100 years old
years_to_100 = 100 - int(user_age)
print(f"You will be 100 years old in {years_to_100} years, in {todays_date.year+years_to_100}")