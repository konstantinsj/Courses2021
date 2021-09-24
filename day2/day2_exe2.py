# 2. Exercise - Room volume

# Ask user to input 3 numbers - width, length, height

width = float(input("Please input width "))
length = float(input("Please input length "))
height = float(input("Please input height "))

# Find the volume of the room

volume = width*length*height

# PS Think about units and what is the most appropriate data type for this
print(f"Volume of the room is {round(volume,2)}")


