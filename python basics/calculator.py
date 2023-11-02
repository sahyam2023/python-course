# def calculator(x, y):
#     """_summary_

#     Args:
#         x (_type_): _Int_
#         y (_type_): _Int_

#     Returns:
#         _type_: _value based on description_
#     """

#     no1 = float(x)
#     no2= float(y)
#     op = input('Pick a operation from the list (+,-,*,/) /n ')
#     if op == '+':
#         return no1+no2
#     elif op== '-':
#         return no1-no2
#     elif op == '*':
#         return no1*no2
#     elif op == '/':
#         return no1/no2

#     value1= input("Enter your first number")
#     value2= input("Enter your second number")

#     output = calculator(value1, value2)
#     if output is not None:
#         print(output)
#     else:
#         print('Error')

#calculator(value1, value2) can't be used as return is being used

#method 2
# def calculator():
#     no1 = float(input('Enter your first number:\n'))
#     no2 = float(input('Enter your second number:\n'))
#     op = input('Pick an operation from the list (+, -, *, /):\n')
    
#     if op == '+':
#         return no1 + no2
#     else:
#         # Handle other operations or exit
#         pass

# # Example usage:
# result = calculator()

# if result is not None:
#      print("Result:", result)
# else:
#      print("Invalid operation or exit.")

# same program with try and catch
# def calculator(x, y):
#     """_summary_

#     Args:
#         x (_type_): _Int_
#         y (_type_): _Int_

#     Returns:
#         _type_: _value based on description_
#     """

#     no1 = float(x)
#     no2= float(y)
#     op = input('Pick a operation from the list (+,-,*,/) /n ')
#     if op == '+':
#         return no1+no2
#     elif op== '-':
#         return no1-no2
#     elif op == '*':
#         return no1*no2
#     elif op == '/':
#         return no1/no2
# try:
#     value1= input("Enter your first number:\n")
#     value2= input("Enter your second number:\n")
#     if not value1 or not value2:
#         raise ValueError("Values can't be empty\n")


#     output = calculator(value1, value2)
#     if output is not None:
#         print(output)
#     else:
#         print('Error')

# except ValueError as e:
#     print(f"Value error: {e}")
# except Exception as e:
#     print(f"error occurred: {e}")    
    
 #With methods only
 
def add(x,y):
     return x+y
def minus(x,y):
     return x+y
def multiply(x,y):
     return x+y
def divide(x,y):
     return x+y

input1 = int(input('number 1:\n'))
input2 = int(input('Number 2:\n'))
check = input('Enter +, -, /, *\n')
if check == '+':
    calc= add(input1, input2)
elif check == '-':
    calc = minus(input1, input2)
elif check == '*':
    calc = multiply(input1, input2)
elif check == '/':
    calc = divide(input1, input2)

print(f'Result is {calc}')