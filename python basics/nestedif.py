number =int(input('Enter your number 1\n'))
secondNumber = int(input('Enter your number 2\n'))
if(number==secondNumber):
    print(f'{number} is equal to {secondNumber}')
else:
    if(number > secondNumber):
        print(f'{number} is greater than {secondNumber}')
    else:
        print(f'{number} is smaller than {secondNumber}')
        