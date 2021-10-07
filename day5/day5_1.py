# The user enters a name.
#
# You print user name in reverse (should begin with capital letter) then extra text: ",a thorough mess is it not ",
# then the first name of the user name then "?"

#name = "Valdis"
name = (input("Whats your name? "))

reverse_name = name[::-1].title()
print(reverse_name)
print(f"{reverse_name}, a thorough mess is it not {name[:1]}?")

