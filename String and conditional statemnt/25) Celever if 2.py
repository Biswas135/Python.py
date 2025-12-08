# take salary input
sal = float(input("Enter your salary: "))

# if salary > 50000 → use 0.2 tax
# else → use 0.1 tax
tax = sal * (0.1, 0.2)[sal > 50000]

print(tax)
