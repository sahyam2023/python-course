import random
name1 = input('Input your name \n')
name2 = input("Input your lover's name \n")

loveScore = random.randint(0,100)
if loveScore <10 or loveScore>85:
    print(f'Your score is {loveScore}, you go together like coke and mentos.')
elif loveScore>=40 and loveScore<=70:
    print(f'Your score is {loveScore},  you are alright together.')
else:
    print(f'Your score is {loveScore},  you are mehh.')

print('Thank You for using our live calculator! come again')
    
    

