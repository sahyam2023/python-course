# def three(ip1, ip2, ip3):
#     if ip1 > ip2 and ip1> ip3:
#         return ip1
#     elif ip2> ip3:
#         return ip2
#     else:
#         return ip3

# lp1 = int(input('Enter number 1:\n'))
# lp2 = int(input('Enter number 2:\n'))
# lp3 = int(input('Enter number 3:\n'))

# print(f'Largest number is:{three(lp1, lp2, lp3)}')


#method 2
def max_of_two(f1, f2):
    if f1> f2:
        return f1
    return f2

def max_of_three(f1, f2, f3):
    g1 = max_of_two(f1, f2)
    mather = max_of_two(g1, f3)
    return mather
print (max_of_three(1,2,3))