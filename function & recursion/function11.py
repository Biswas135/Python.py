# WAP to calculate the sum of n natural numbers using recursion

def cal_sum(n):
    if n == 0:           # base condition: sum of 0 numbers is 0
        return 0
    else:
        return cal_sum(n-1) + n   # recursive call

sum_result = cal_sum(5)          # calculate sum of first 5 natural numbers
print(sum_result)
