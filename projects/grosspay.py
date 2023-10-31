hours = int(input('Enter Hours\n'))
rate = float(input('Enter Rate\n'))
if hours < 40:
    pay= round (hours *rate, 2)
else:
    overtime = hours-40
    pay= round(40 * rate + overtime *rate*1.5, 2)

print(f'Your pay is {pay}')