print('Welcome to the trip cost Calculator\n')
stayDays = int(input('How many days will you stay\n'))
hostelCost = float(input('How much does the hotel cost per night\n INR '))
flightPrice = float(input('How much does your transport cost\n INR '))
rentalCar = float(input('If you need a rental car type your expected cost otherwise type 0\n INR '))
otherExpenses = float(input('Type your other expenses if any otherwise type 0\n INR '))
costEstimate = round(stayDays * hostelCost + flightPrice + stayDays * rentalCar + otherExpenses, 2)
print(f'Your total trip cost estimate will be {costEstimate} INR')
