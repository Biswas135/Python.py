# WAP to print the length of a list (list is the parameter)

cities = ["KTM", "PKR", "BANEPA", "LALITPUR"]     # list of cities
heroes = ["BALEN", "KULMAN", "RAJU"]              # list of heroes

def print_len(list):          # function that takes a list as parameter
    print(len(list))          # prints the length of the list

print_len(cities)             # prints length of cities list → 4
print_len(heroes)             # prints length of heroes list → 3
