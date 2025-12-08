# take age input and convert to integer
age = int(input("Enter your age: "))

# using tuple indexing to check voting eligibility
# if age < 18 → index becomes 1 → "No"
# if age >= 18 → index becomes 0 → "Yes"
vote = ("Yes", "No")[age < 18]

# print result
print(vote)
