
from array import *

# 1. Create an array and traverse

arr1= array('i',[1,2,3,4,5,6])
for i in arr1:
    print(i)

# 2. Acess individual elements through indexes.

print("step 2")
print(arr1[4])

# 3. append any value to the array using append() method

print('step 3')
arr1.append(7)
print(arr1)

#4. insert value in an array using insert method.

print('step 4')
arr1.insert(1,8)
print(arr1)

# 5. extend python array using extend() method.

print('step 5')
my_arr=array('i',[10,11,23])
arr1.extend(my_arr)
print(arr1)

# 6. Add items from list into array using from list() method.

print('step 6')
templist=[20,21,22]
arr1.fromlist(templist)
print(arr1)

# 7. remove any array element using remove() method.

print('step 7')
arr1.remove(22)
print(arr1)

# 8. remove last array element using pop() method.

print('step 8')
arr1.pop()
print(arr1)

# 9.Fetch any element through its index using index() method.

print('step 9')
print(arr1.index(23))

# 10. Reverse a python array using reverse() method.

print('step 10')
arr1.reverse()
print(arr1)

# 11. Get array buffer information through buffer_info( ) method.

print('step 11')
print(arr1.buffer_info())

# 12. Check for no. of occurences of an element using count() method.

print('step 12')
arr1.append(11)
print(arr1.count(11))

# 13. Convert array to string using tostring() method.

print('step 13')
strTemp=arr1.tostring()
print(strTemp)

ints=array('i')
ints.fromstring(strTemp)
print(ints)

# 14. Convert array to a python list with same elemnts using tolist() method.

print('step 14')
print(arr1.tolist())

# 15. Append a string to char array using fromstring() method.

# 16. Slice element from an arary
print('step 16')
print(arr1[1:4])



