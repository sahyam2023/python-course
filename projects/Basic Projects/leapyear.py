leapYear= int(input('Enter your year\n'))
if leapYear % 4 !=0:
    print ('Not a leap year')
elif leapYear % 4 ==0:
    if leapYear % 100 ==0:
        if leapYear % 400==0:
            print('leap year')
        else:
            print('Not a leap year')
    else:
        print('leap year')
            
    

