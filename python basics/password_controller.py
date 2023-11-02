#password checker and also docstring
def check(password):
    """_summary_

    Args:
        password (_type_): _Takes string input_

    Returns:
        _type_: _Returns True or False based on length of password_
    """
    check_len = len(password)
    if check_len > 8:
        return True
    else:
        return False

value = input('Enter your password\n')
output = check(value)
print(output)
    