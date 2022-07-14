#To find greatest common divisior of two nos using recursion

def gcd(a,b):
    assert int(a)==a and int(b)==b,'The nos must be integer only'
    if a<0:
        a=-1*a
    if b<0:
        b=-1*b    

    if b==0:
        return a
    else:
        return gcd(b,a%b)

   


print(gcd(1025,4.5))    