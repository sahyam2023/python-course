print("welcome to my calulator")
Rate=0
salary = int(input('Enter your salary \n'))
if(salary > 2000):
    creditScore = int(input('Enter your credit score \n'))
    if(creditScore > 800):
        Rate=4
        print('Your are eligible for morgage and your interest rate can be 4%')
    elif(creditScore >600 and creditScore<800):
        Rate=5
        print('Your are eligible for morgage and your interest rate can be 5%')
    else:
        Rate=6
        print('Your are eligible for morgage and your interest rate can be 6%')
    disability = input("Do you have any disability? Type y for Yes and n for No\n")
    if disability == 'y':
        Rate -= 2
        print(f'You got a discount and now your final Interest rate is{Rate}%')
    else:
        Rate = Rate
        print(f'Sorry, your interest rate is still the same i.e {Rate}%.')
else:
    print('Sorry you are not eligible for morgage')
