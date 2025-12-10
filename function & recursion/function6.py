# WAP to print the elements of a list in a single line (list is the parameter)

friends = ["MONICA", "PHOEBE", "JOEY", "ROSS", "CHANDLER", "RACHEL"]

def print_len(list):
    print(len(list))        # prints the number of elements

def print_list(list):
    for item in list:       # correct loop syntax
        print(item, end=" ")  # print items in same line with space

print_list(friends)
