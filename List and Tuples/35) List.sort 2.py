list=[2,1,3]
list.sort(reverse=True)
print(list)


""" [also work dor string ]
list=[banana,apple,mango,cake]
print(list.sort(reverse=True))
print(list)
"""# Sorting numbers in descending order
list = [2, 1, 3]            
list.sort(reverse=True)     # reverse=True → sort from highest to lowest
print(list)                 # output: [3, 2, 1]

"""
Also works for strings
"""

# Sorting strings in descending (reverse alphabetical) order
list = ["banana", "apple", "mango", "cake"]  
list.sort(reverse=True)     # sort alphabetically in reverse
print(list)                 # output: ['mango', 'cake', 'banana', 'apple']
