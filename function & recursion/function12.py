# Write a recursion function to print all elements in a list
# Hint: Use list & index as parameters

def print_list(list, idx=0):          # idx has default value 0
    if idx == len(list):              # base condition: stop when index reaches length
        return
    print(list[idx])                  # print current element
    print_list(list, idx + 1)        # recursive call with next index

fruits = ["mango", "litchi", "apple", "banana"]
print_list(fruits)                    # call the function
