def password_controller(password):
    if len(password) > 8:
        return True
    else:
        return False

#print(password_controller(123456))
password_list = ['qwerty', 'Quem', 'Helo', 'Hugh']

for passWord in password_list:
    result= password_controller(password_list)
    print(passWord, result)
    # print(password_controller(password_list))