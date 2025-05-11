def is_valid_email(email):
    #  @ symbol
    if email.count('@') != 1:
        return False

    start, domain= email.split('@')


    if not start or not domain:
        return False

    if '.' not in domain or domain.startswith('.') or domain.endswith('.'):
        return False
    allowed_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._+-"
    for char in start:
        if char not in allowed_chars:
            return False


    allowed_domain_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-"
    for char in domain:
        if char not in allowed_domain_chars:
            return False

    parts = domain.split('.')
    if len(parts[-1]) < 2:
        return False

    return True

mail = input('Enter the email address')
if is_valid_email(mail):
    print("Email is valid")
else:
    print("Email is not valid")
