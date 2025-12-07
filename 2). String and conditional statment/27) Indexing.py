# define a string
str = "apna_collage"
      #0123456789
      
# access first character
ch = str[0]
print(ch)  # output: 'a'

# access 6th character (index 5)
print(str[5])  # output: 'c'

"""
Strings are immutable in Python, which means
we cannot change a character directly.

For example:

str = "apna_collage"
str[4] = "a"  # ❌ This will cause an error
print(str)
"""
