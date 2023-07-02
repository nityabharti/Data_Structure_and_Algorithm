# 27.CREATE AN ARRAY

import array

arr=array.array('i')
print(arr)
arr1=array.array('i',[1,2,3,4,5,6])
print(arr1)


import numpy as np
np_arr=np.array([],dtype=int)
print(np_arr)
np_arr1=np.array([1,2,4,5,3])
print(np_arr1)


# 28. INSERTION TO ARRAY

arr_2=[1,2,3,4,5]
arr_2.insert(0,6)
print(arr_2)


# 29. TRAVERSal OPERATION

def traverseArray(array):
    for i in array:
        print(i)
traverseArray(arr_2) 

# 30.   ACESSING AN Element OF ARRAY

def aceessElement(array,index):
    if index>len(array):
        print("not any element")
    else:
        print(array[index])
aceessElement(arr_2,0)
      
     
# 31. SEARCHING AN ELEMENT OF ARRAY

my_arr=[3,5,6,8,9,2]
def linear_search(arr,target):
    for i in arr:
        if arr[i]==target:
            return i
    return -1
print(linear_search(my_arr,2))
           
    
# 32. DELETING AN ELEMENT FROM AN ARRAY

from array import *

my_arr1=array('i',[1,2,3,4,5,6])
my_arr1.remove(2)
print(my_arr1)