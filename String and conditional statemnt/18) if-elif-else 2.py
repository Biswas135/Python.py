# take marks input and convert to integer
marks = int(input("Enter your marks: "))

# check grading conditions
if marks >= 90:
    print("A")
elif marks >= 80 and marks < 90:
    print("B")
elif marks >= 70 and marks < 80:
    print("C")
else:
    print("D")
