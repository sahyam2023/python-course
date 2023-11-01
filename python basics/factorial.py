import math
try:
    number = int(input('Enter your number'))
    answer= math.factorial(number)
except ValueError:
    print('Stupid integer positive number only')
    exit()
else:
    print(f'The factorial of {number} is: {answer}')