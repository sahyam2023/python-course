name1 = input('Input your name \n')
name2 = input("Input your lover's name \n")
name1= name1.lower()
name2= name2.lower()
tCount = name1.count('t')
tCount2 = name2.count('t')

rCount = name1.count('r')
rCount2 = name2.count('r')

uCount = name1.count('u')
uCount2 = name2.count('u')

eCount = name1.count('e')
eCount2 = name2.count('e')

lCount = name1.count('l')
lCount2 = name2.count('l')

oCount = name1.count('o')
oCount2 = name2.count('o')

vCount = name1.count('v')
vCount2 = name2.count('v')

eCount = name1.count('e')
eCount2 = name2.count('e')

overallCount1 = tCount+rCount+uCount+eCount+tCount2+rCount2+uCount2+eCount2
overallCount2= lCount+oCount+vCount+eCount+lCount2+oCount2+vCount2+eCount2

loveScore = str(overallCount1) + str(overallCount2)
loveScore = int(loveScore)
if loveScore <10 or loveScore>85:
    print(f'Your score is {loveScore}, you go together like coke and mentos.')
elif loveScore>=40 and loveScore<=70:
    print(f'Your score is {loveScore},  you are alright together.')
else:
    print(f'Your score is {loveScore},  you are mehh.')

print('Thank You for using our live calculator! come again')
    
    

