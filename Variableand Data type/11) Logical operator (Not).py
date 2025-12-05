a = 50
b = 30

# not operator always gives the opposite (reverse) boolean value
print(not False)      # False becomes True
print(not True)       # True becomes False

# Check if a is greater than b → result is True, but "not" makes it False
print(not(a > b))     # a > b → True → not True → False

# Check if a is less than b → result is False, but "not" makes it True
print(not(a < b))     # a < b → False → not False → True
