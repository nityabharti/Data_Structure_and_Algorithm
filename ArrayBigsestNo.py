#find the biggest number of the array
sampleArray=[2,8,5,87,10,49,88,97,2,4,6,3]     
def findBiggestNumber (sampleArray):
    BiggestNumber=sampleArray[0]
    for index in range (1,len(sampleArray)):
        if sampleArray[index]>BiggestNumber:
            BiggestNumber=sampleArray[index]
        return BiggestNumber    
    print(BiggestNumber)    
    
    
