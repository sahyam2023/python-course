# from array import *

# array1 = ('i', [1,2,3,4,5,6,7,8])

# def linear_search(arr, search_Value):
#     for i in range(len(arr)):
#         if arr[i] == search_Value:
#             #return i
#             print(f'index is {i}')
#             #return -1
#     print (-1)

# linear_search(array1, 5)

##practice REQUIRED

#mport array
from array import*
#create array
arrays = array('i', [2,4,6,8,10])
#define the function with parameters(mandatory)
def arrayLinear(arr, target):
    for i in range(len(arr)):
        if arr[i]== target:
            return i
    return -1

print(arrayLinear(arrays, 10))

#we always print the index not the element in the index
#linear search searches the index and prints it if the element in th index is found, it ill print the index