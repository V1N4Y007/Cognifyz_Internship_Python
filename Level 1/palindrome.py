def palindrome(str):
    return str == str[::-1]
str = input('Enter the string: ')
if palindrome(str):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")