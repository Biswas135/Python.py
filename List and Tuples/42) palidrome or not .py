#Check whether palidrom or not 
list1 = ["m", "a", "d", "a", "m"]     # original list
copy_list1 = list1.copy()             # make a copy of the list
copy_list1.reverse()                  # reverse the copied list

if(copy_list1 == list1):              # compare reversed list with original
    print("Palindrome")               # if same → it's a palindrome
else:
    print("Not Palindrome")           # otherwise → not palindrome
