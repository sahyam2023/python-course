height = float(input("Enter your height in m: \n"))
weight =  float(input("Enter your weight in kg: \n"))
Bmi = round(weight/height**2, 1)
print(f'Your BMI is {Bmi}')
if(Bmi<18.5):
    print('You are underweight')
elif(Bmi>18.5 and Bmi<25):
    print('You are normal')
elif(Bmi>25 and Bmi<30):
    print('you are overweight')
elif(Bmi>30 and Bmi<35):
    print('You are obese')
    