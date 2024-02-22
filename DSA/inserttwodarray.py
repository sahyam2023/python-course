import numpy as np

twoDArray= np.array([[1,2,3,4,5], [11,12,13,14,15], [21,22,23,24,25], [31,32,33,34,35]])

newTwoDArray= np.insert(twoDArray, 0, [[100,101,102,103]], axis= 1)  #which array to integrate with, on which index, which elements, on column or row
#axis 0 means row, 1 means column
print(newTwoDArray)