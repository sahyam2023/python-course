def year(x):
    if x % 4 == 0:
        if x % 100 ==0:
            if x % 400 ==0:
                return 'leap year'
            else:
                return ' not a leap year'
        else:
            return 'leap year'
    else:
        return 'not a leap year'
