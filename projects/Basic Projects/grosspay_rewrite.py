def compute_pay(p_hour, p_rate):
    if p_hour < 40:
        pay= round (p_hour *p_rate, 2)
    else:
        overtime = p_hour-40
        pay= round(40 * p_rate + overtime *p_rate*1.5, 2)
    return pay
def checks(input1):
    try:
        val = float(input1)
        return val
    except ValueError:
        print("enter valid data")
        quit()
hours = input('Enter Hours\n')
hours= checks(hours)
rate = input('Enter Rate\n')
rate = checks(rate)
output= compute_pay(hours,rate)
print(f"pay is{output}")


