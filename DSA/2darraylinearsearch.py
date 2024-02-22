import numpy as np

twoDArray= np.array([[1,2,3,4,5], [11,12,13,14,15], [21,22,23,24,25], [31,32,33,34,35]])
print(twoDArray)

def twoArraySearch(array, target):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j]== target:
                return 'Element found at Index '+ str(i)+" "+str(j)
    return 'Not found'

print(twoArraySearch(twoDArray, 3))