def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

n1 = int(input("What is the first number? "))
n2 = int(input("What is the second number? "))
operation = input("Pick operation from this list (+,-,*,/) ")

def calculate(n1,n2,operation):
    if operation == "+":
        answer = add(n1,n2)
    elif operation == "-":
        answer = subtract(n1,n2)
    elif operation == "*":
        answer = multiply(n1,n2)
    elif operation == "/":
        answer = divide(n1,n2)
    return answer

output = calculate(n1,n2,operation)

print(f"{n1} {operation} {n2} = {output}")

new_operation = input("Pick another operation from this list (+,-,*,/) ")
n3 = int(input("What is the third number? "))

new_output = calculate(calculate(n1,n2,operation), n3, new_operation)

print(f"{output} {new_operation} {n3} = {new_output}")
