# 1. Health check

# Ask user for their temperature.

35

# If the user enters below 35, then output "not too cold"
if user_temperature < 35:
    print("Not too cold")

# If 35 to 37 (inclusive), output "all right"
if 35 <= user_temperature <= 37:
    print("Alright")

# If the temperature  over 37, then output  "possible fever"
if 37 < user_temperature:
    print("possible fever!")