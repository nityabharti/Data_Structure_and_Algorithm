#How to calculate power of a number using recursion?

def power(base ,exp):
    assert exp>=0 and int(exp)==exp,'The exponent must me positive only'
    if exp==0:
        return 1
    if exp==1:
        return base
    return base*power(base,exp-1)

print(power(2,-1))    