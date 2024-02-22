import numpy as np

twodArray= np.array([[1,2,3,4,5], [11,12,13,14,15], [21,22,23,24,25], [31,32,33,34,35]])
print(twodArray)

def accessArray(array, rowIndex, columnIndex):
    if rowIndex >= len(array) or columnIndex>=len(array[0]):
        print('out of bounds')
    
    else:
        print(array[rowIndex][columnIndex])
    
accessArray(twodArray, 1, 2)