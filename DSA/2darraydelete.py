import numpy as np

twoDArray= np.array([[1,2,3,4,5], [11,12,13,14,15], [21,22,23,24,25], [31,32,33,34,35]])
print(twoDArray)

newTDArray= np.delete(twoDArray, 3, axis=1)
print(newTDArray)
