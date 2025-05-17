password = input('Enter the password: ')
def hasDigit(password):
    for c in password:
        if c.isdigit():
            return True
    return False


def specialCharacters(password):
    for c in password:
        if c in ['@','$','#','!','&','%']:
            return True
    return False


if len(password) < 8:
    print('Password is too short')
elif password.isupper() or password.islower():
    print('Password should have both uppercase and lowercase letters')
elif hasDigit(password) == False:
    print('Password should have atleast one digit')
elif specialCharacters(password) == False:
    print('passowrd should have atleast one special character')
else:
    print('password is strong')