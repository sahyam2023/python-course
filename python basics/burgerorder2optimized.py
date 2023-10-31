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

mini_burger = 5
normal_burger = 8
large_burger = 10
extra_mushroom = 1
extra_mushroom_large = 2
extra_cheese = 1

burger_select = input('Select the type of burger you want to eat and type the burger code\n')

if burger_select == 'M':
    mushroom = input('Do you want extra mushroom? Type y for yes and n for No\n')
    cheese = input('Do you want extra cheese? Type y for yes and n for No\n')
    bill = mini_burger + (extra_mushroom if mushroom == 'y' else 0) + (extra_cheese if cheese == 'y' else 0)
elif burger_select == 'N':
    mushroom = input('Do you want extra mushroom? Type y for yes and n for No\n')
    cheese = input('Do you want extra cheese? Type y for yes and n for No\n')
    bill = normal_burger + (extra_mushroom if mushroom == 'y' else 0) + (extra_cheese if cheese == 'y' else 0)
elif burger_select == 'L':
    mushroom = input('Do you want extra mushroom? Type y for yes and n for No\n')
    cheese = input('Do you want extra cheese? Type y for yes and n for No\n')
    bill = large_burger + (extra_mushroom_large if mushroom == 'y' else 0) + (extra_cheese if cheese == 'y' else 0)
else:
    print('Invalid selection')
    exit()

print(f'Your total bill is ${bill}. \n Thank you for eating in our restaurant')
