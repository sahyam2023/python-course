def add_odd_numbers():
    sum = 0
    for odd in range(1,100,2):
        sum+=odd
    return sum
print(add_odd_numbers())