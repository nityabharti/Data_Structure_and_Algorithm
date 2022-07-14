# How to find the sum of digits of a positive number using recursion

def sumOfDigit(n):
    assert n>=0 and int(n)==n,'sum of positive no. is always positive '
    if n ==0:
        return 0
    else:
        return int(n%10) +sumOfDigit(int(n/10))

print(sumOfDigit(12345))
