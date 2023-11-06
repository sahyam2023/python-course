# Numbers Divisible by 5 Until 130
# Implement a function which takes a given ordered list as a parameter and displays numbers divisible by 5 and if a number is greater than 130 display STOP in the console.
list1 = [12, 15, 32, 40, 52, 75, 122, 132, 150, 180, 200]
def numbers_divisible_byfive(p_list):
    for lists in list1:
        if lists % 5 == 0:
            print (lists)
        if lists > 130:
            break
    print('stopped')
numbers_divisible_byfive(list1)
