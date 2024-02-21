str= input('ENter string: ')
helos= str.casefold()
rev= reversed(str)


if list(str)==list(rev):
    print('Pallindrome')
else:
    print('not pallindrome')