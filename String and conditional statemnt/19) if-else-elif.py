# ask the user to enter a traffic light colour
light = input("Enter your colour: ")

# check if the light is red
if light == "red":
    print("Stop")

# check if the light is yellow
elif light == "yellow":
    print("Look")

# check if the light is green
elif light == "green":
    print("GO")

# if none of the colours match
else:
    print("Invalid")
