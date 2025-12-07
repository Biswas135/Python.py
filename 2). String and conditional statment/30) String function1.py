# define string
str = "i am starting python from appnacollage"

# check if string ends with 'age'
print(str.endswith("age"))  
# True → because the string ends with 'age'

# capitalize first character of the string
print(str.capitalize())  
# 'I am starting python from appnacollage'

# replace substring 'appnacollage' with 'gurukul'
print(str.replace("appnacollage", "gurukul"))  
# 'i am starting python from gurukul'

# find first occurrence of 'o' in string
print(str.find("o"))  
# index of first 'o', output: 14

# count number of occurrences of 'a'
print(str.count("a"))  
# output: 6
