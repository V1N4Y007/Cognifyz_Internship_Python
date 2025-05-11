def convert(value,unit):
    if unit=='fahrenheit':
        return (value-32)*5/9
    else:
        return (value*9/5)+32

temp = int(input('Enter temperature'))
unit = input('Enter Unit (celsius or fahrenheit)')

print(convert(temp,unit))