# Recursion function example:

def show(n):
    if n == 0:      # Base condition
        return
    print(n)        # Print current number
    show(n - 1)     # Recursive call (n decreases by 1)

show(5)
