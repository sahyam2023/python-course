
from array import *

arr1= array('i', [1,2,3,4,5,6,7])

def linearSearch(arr2, searchTarget):
    for i in range(len(arr2)):
        if arr2[i]==searchTarget:
            return i
    return -1

print(linearSearch(arr1, 5))
#okay i remember how to do it
