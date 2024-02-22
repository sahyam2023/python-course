import numpy as np

twodArray= np.array([[1,2,3,4,5], [11,12,13,14,15], [21,22,23,24,25], [31,32,33,34,35]])

def traverse(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

traverse(twodArray)