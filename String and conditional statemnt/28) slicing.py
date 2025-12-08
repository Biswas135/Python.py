# define string
str = "apna collage"

# slice from index 1 to 3 (4 not included)
print(str[1:4])  # output: 'pna'

# slice from index 0 to 3
print(str[0:4])  # output: 'apna'

# slice from index 5 to 11 (12 not included)
print(str[5:12])  # output: 'collage'

# slice from index 5 to end
print(str[5:len(str)])  # output: 'collage'

# slice from start to index 3
print(str[:4])  # output: 'apna'

# slice from index 1 to end
print(str[1:])  # output: 'pna collage'
