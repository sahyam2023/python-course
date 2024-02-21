from array import *
arr1= array('i', [2,3,4,5,6,7,8]) #write array when accessing array

def accessArray(array, index):
    if index >= len(array): #COZ IF WE WRITE 7 IT WILL SHOW ERROR AS LENGTH IS 7 AND WE ADDED > LEN . SO FIX WE NEED TO ADD >= LENGTH AS LENGTH IS GREATER THAN INDEX BY 1 ALWAYS
        print('Index out of Bounds')
    else:
        print(array[index]) #ACCESSING THE ARRAY WHICH IS AR1 AND IT'S INDEX VALUES

accessArray(arr1, 7)