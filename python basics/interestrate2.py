print("Welcome to my calculator")
Rate = 0

while True:
    try:
        salary = int(input('Enter your salary \n'))
        break  # If input is successful, exit the loop
    except ValueError:
        print('Please enter salary in numeric value only')

if salary > 2000:
    credit_score = int(input('Enter your credit score \n'))

    if credit_score > 800:
        Rate = 4
        print('You are eligible for a mortgage, and your interest rate can be 4%')
    elif 600 <= credit_score <= 800:
        Rate = 5
        print('You are eligible for a mortgage, and your interest rate can be 5%')
    else:
        Rate = 6
        print('You are eligible for a mortgage, and your interest rate can be 6%')

    disability = input("Do you have any disability? Type y for Yes and n for No\n")
    if disability == 'y':
        Rate -= 2
        print(f'You got a discount, and now your final Interest rate is {Rate}%')
    else:
        print(f'Sorry, your interest rate is still the same, i.e., {Rate}%.')
else:
    print('Sorry, you are not eligible for a mortgage')

print('Thank you for using my interest rate calculator! Come again')
