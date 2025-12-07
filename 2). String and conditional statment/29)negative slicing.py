# define string
str = "apple"

# slice using negative indices
print(str[-5:-2])  # output: 'app'
# Explanation: -5 → 'a', -2 → 'l' (not included), so 'app'

print(str[-4:-1])  # output: 'ppl'
# Explanation: -4 → 'p', -1 → 'e' (not included), so 'ppl'
