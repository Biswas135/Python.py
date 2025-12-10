# Factorial using recursion

def fact(n):
    if n == 0 or n == 1:   # base condition: factorial of 0 or 1 is 1
        return 1
    else:
        return n * fact(n-1)  # recursive call

result = fact(5)          # call the function with 5
print(result)             # print the factorial
