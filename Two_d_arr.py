
# Day1 - 11,15,10,6
# Day2 - 10,14,11,5
# Day3 - 12,17,12,8
# Day4 - 15,18,14,9


import numpy as np
twoDArr=np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(twoDArr)

# 36. INSERTION

# new_2DArr=np.insert(twoDArr,2,[[1,2,3,4]],axis=1)
# print(new_2DArr)

new_2DArr=np.append(twoDArr,[[1,2,3,4]],axis=0)
print(new_2DArr)

# 37. ACCESSING AN ELEMENT OF 2D ARRAY

def accessElement(array,rowInd,colInd):
    if rowInd>=len(array) and colInd>= len(array[0]):
        print("Incorrect index")
    else:
        print(array[rowInd][colInd])
accessElement(twoDArr,2,3)

# 38. TRAVERSING

print("Traversing\n")

def traverseTDArr(array):
    for i in range (len(array)):
        for j in range (len(array[0])):
            print(array[i][j])

traverseTDArr(twoDArr)

# 38. SEARCHING

print("Searching\n")
print(twoDArr)
def searchTDArr(array,value):
    for i in range (len(array)):
        for j in range (len(array[0])):
            if array[i][j]==value:
                return 'The val is located at index ' + str(i) +" "+str(j)
    return 'Element not found'

print(searchTDArr(twoDArr,18))

# 38. DELETION


print("Deletion\n")
new_2D_Arr=np.delete(twoDArr,1,axis=1)
print(new_2D_Arr)





