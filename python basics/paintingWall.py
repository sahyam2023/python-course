# Question:
#     Painting the Wall
# We need to paint a wall and we do not know how many cans of paint we need to buy. The instructions on the paint can says that 1 can of paint can cover 4 square meters of wall. So we need to define a function which takes as parameter  height and width of wall and  calculates the area of the wall and based on the area we can calculate number of cans of paint that we need.

# Area of wall = wall height  *  wall width

# Number of cans of paint that is needed =  Area of wall ÷ coverage per can.

# Example

# Height = 2, Width = 5, Coverage = 4

# Area of wall = 2  *  5  = 10

# Number of cans of paint that is needed =  10 ÷ 4 = 2.5

# But because you can't buy 2.5 of a can of paint, the result should be rounded up to 3 cans.

# Hint: To round up number ceil function from math module can be used. Math.ceil()

#method 1
# import math
# def wallPainting():
#     height = float(input('Enter the height of wall'))
#     width = float(input('Enter the width of the wall'))
#     coverage= float(input('enter the coverage area'))
#     Area= height * width
#     nOfCans = Area / coverage
#     nOfCans= math.ceil(nOfCans)
#     print(f'The number of can u need is {nOfCans}')

# wallPainting()

#method2 predifined
import math
def wallPainting(height, width, coverage):
    Area= height * width
    nOfCans = Area / coverage
    nOfCans = math.ceil(nOfCans)
    print(f'The number of can u need is {nOfCans}')

wallPainting(width=5, coverage=4, height=2)

    


                   