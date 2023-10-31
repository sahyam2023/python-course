# Burger Order
# Write a program that calculates final bill Burger Order Price based on a user's choice.

# Price List.

# Mini Burger (M) : $5

# Normal Burger (N): $8

# Large Burger (L) : $10

# Add Mushroom : For Mini and Normal = $1, For Large = $2

# Extra Cheese : $1


# Example Input

# size = "N"
# add_mushroom = "Y"
# extra_cheese = "N"
# Example Output

# Your final bill is: $9.

print('Welcome to sahyam\'s restaurant')
print('Here\'s our menu \n #Mini Burger (M): 5$ \n #Normal Burger (N): 8$ \n #Large Burger (L): 10$ \n #Extra Mushroom for Both N and M: $1 \n #Extra Mushroom for L: $2 \n #Extra cheese: $1')
miniBurger= 5
largeBurger =10
normalBurger =8
extraMushroom=1
extraMushroomLarge=2
extraCheese=1
bill=0
burgerSelect =input('Select the type of burger you want to eat and type the burger code\n')
if burgerSelect == 'M':
    mushroom= input('Do you want to extra mushroom? Type y for yes and n for No\n')
    Cheese = input('Do you want to extra cheese? Type y for yes and n for No\n')
    if mushroom == 'y' and Cheese == 'y':
        bill= miniBurger+extraMushroom+extraCheese
    elif mushroom == 'n' and Cheese == 'y':
        bill= miniBurger+extraCheese
    elif mushroom == 'y' and Cheese == 'n':
        bill= miniBurger+extraMushroom
    elif mushroom == 'n' and Cheese == 'n':
        bill= miniBurger
elif burgerSelect == 'N':
    mushroom= input('Do you want to extra mushroom? Type y for yes and n for No\n')
    Cheese = input('Do you want to extra cheese? Type y for yes and n for No\n')
    if mushroom == 'y' and Cheese == 'y':
        bill= normalBurger+extraMushroom+extraCheese
    elif mushroom == 'n' and Cheese == 'y':
        bill= normalBurger+extraCheese
    elif mushroom == 'y' and Cheese == 'n':
        bill= normalBurger+extraMushroom
    elif mushroom == 'n' and Cheese == 'n':
        bill= normalBurger
elif burgerSelect == 'L':
    mushroom= input('Do you want to extra mushroom? Type y for yes and n for No\n')
    Cheese = input('Do you want to extra cheese? Type y for yes and n for No\n')
    if mushroom == 'y' and Cheese == 'y':
        bill= largeBurger+extraMushroomLarge+extraCheese
    elif mushroom == 'n' and Cheese == 'y':
        bill= largeBurger+extraCheese
    elif mushroom == 'y' and Cheese == 'n':
        bill= largeBurger+extraMushroomLarge
    elif mushroom == 'n' and extraCheese == 'n':
        bill= largeBurger
else:
    print('Invalid selection')
    exit()
print(f'Your total bill is ${bill}. \n Thank You for eating in our restaurant')