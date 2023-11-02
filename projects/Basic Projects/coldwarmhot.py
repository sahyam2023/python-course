def cwh(temp):
    if temp > 28:
        return 'Hot'
    elif temp >=18 and temp <=28:
        return 'warm'
    elif temp < 18:
        return 'cold'

input1 = int(input('Enter your temperature\n'))

output = cwh(input1)
print(output)
    