# take age input
A = int(input("A: "))

# take gender input
G = input("M/F : ")

# condition 1: age is 1 or 2 AND gender is male
if (A == 1 or A == 2) and G == "M":
    print("fee is 100")

# condition 2: age is 3 or 4 OR gender is female
elif (A == 3 or A == 4) or G == "F":
    print("fee is 200")

# condition 3: age is 5 AND gender is male
elif A == 5 and G == "M":
    print("fee is 300")

# all other cases
else:
    print("No fee")
