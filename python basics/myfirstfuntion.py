#contains positional argumens, keyword arguments and basic functions
def my_first_function():
    print("This is my first function")
    print("Really exicted to learn functions tbh")
    print("Bye for now")
#calling the function
my_first_function()

def greet(name):
    print(f'Hi {name}')

greet('heyworld')

def greet_with_nc(name, city):
    print(f'My name is {name}')
    print(f'My city is {city}')

greet_with_nc(city='newyork', name='heyworld')