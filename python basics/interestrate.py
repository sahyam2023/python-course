print("welcome to my calulator")
salary = int(input('Enter your salary \n'))
if(salary < 2000):
    print(f'sorry no morgage for you')
else:
    creditScore = int(input('Enter your credit score \n'))
    if(creditScore > 800):
        print('Your are eligible for morgage and your interest rate will be 4%')
    elif(creditScore >600 and creditScore<800):
        print('Your are eligible for morgage and your interest rate will be 5%')
    else:
        print('Your are eligible for morgage and your interest rate will be 6%')
