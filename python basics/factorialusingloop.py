# def factorial(p_num):
#     result=1
#     if p_num < 0:
#         return 'Factorial doesnt exist for negative number'
#     if p_num == 0:
#         return 1
#     if p_num> 0:
#         for fact in range(1, p_num+1):
#             result*=fact
#         return result
# output = int(input('enter a number: '))
# if output > 0:
#     print(f'The factorial of {output} is {factorial(output)}')
# else:
#     print(factorial(output))

#method 2
def factorial(p_num):
    result = 1
    if p_num < 0:
        return 'Factorial does not exist for negative numbers'
    for fact in range(1, p_num + 1):
        result *= fact
    return result

output = int(input('Enter a number: '))
if output < 0:
    print(factorial(output))
elif output == 0:
    print(f'The factorial of {output} is 1')
else:
    print(f'The factorial of {output} is {factorial(output)}')
