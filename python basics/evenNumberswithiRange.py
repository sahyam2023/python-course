def add_even_numbers(start, end):
    sum= 0
    for even in range(start, end+1):
        if even % 2==0:
            sum+=even
    return sum
no1= int(input('Enter number 1 \n'))
no2 = int(input('Enter number 2 \n'))

print(add_even_numbers(no1, no2))
