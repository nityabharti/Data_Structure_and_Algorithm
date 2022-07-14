# import sys
# sys.setrecursionlimit(1000)
# def factorial(n):
#     assert n>=0 and int(n)==n,'The number must be positi'
#     if n in [0,1]:
#         return n
#     else:
#         return n*factorial(n-1)    
# print(factorial(4)) 

def fabonacci(n):
    assert n>=0 and int(n)==n,'Fibonacci number can not be negative number or non integer'
    if n in [0,1]:
        return n
    else:
        return fabonacci(n-1) + fabonacci(n-2)    
print(fabonacci(6.4))       