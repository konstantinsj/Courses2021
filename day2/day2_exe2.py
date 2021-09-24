# 2. Exercise - Room volume

# Ask user to input 3 numbers - width, length, height
# Find the volume of the room
# PS Think about units and what is the most appropriate data type for this

width = float(input("Please input width "))
length = float(input("Please input length "))
height = float(input("Please input height "))
volume = width*length*height
print(f"Volume of the room is {round(volume,2)}")