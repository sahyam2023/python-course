try:
    hours = int(input('Enter Hours\n'))
    rate = float(input('Enter Rate\n'))
except ValueError:
    print('enter only integer value and try again')
    exit()
if hours < 40:
    pay= round (hours *rate, 2)
else:
    overtime = hours-40
    pay= round(40 * rate + overtime *rate*1.5, 2)

print(f'Your pay is {pay}')