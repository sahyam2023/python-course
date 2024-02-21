import array

my_array= array.array('i', [1,2,3,4,5])

# arrays= my_array.insert(3,9)
# print(arrays) # shows none because insert returns 0

#my_array.insert(3,9)
#print(my_array) #directly modifies the the my_array as list and arrays are mutable

def traverseArray(array): #define please
    for i in array: #use the define 
        print(i)

traverseArray(my_array) 
