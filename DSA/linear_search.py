
from array import *

array1 = array('i', [1,2,3,4,5,6,7,8])

def linear_search(arr, search_Value):
    for i in range(len(arr)):
        if arr[i] == search_Value:
            return i
    return -1
print(linear_search(array1, 5))