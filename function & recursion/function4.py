# Default Parameters
# assigning a default value to parameters, which is used when no argument is passed

def cal_product(a=4, b=2):   # a and b have default values
    product = a * b         # multiply the numbers
    return product          # return the result

print(cal_product())        # uses default values → 4 * 2 = 8
print(cal_product(5, 3))    # uses given arguments → 5 * 3 = 15
print(cal_product(10))      # only 'a' is given, b stays default → 10 * 2 = 20
