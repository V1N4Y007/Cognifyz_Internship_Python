def calc(num1,num2,operator):
    if operator == '+':
        print(num1 + num2)
    elif operator == '-':
        print(num1-num2)
    elif operator == '*':
        print(num1*num2)
    elif operator == '/':
        if num2 != 0:
            print(num1/num2)
        else:
            print('Error! Division by zero is not allowed')
    elif operator == '%':
        if num2 != 0:
            print(num1%num2)
        else:
            print('Error! Division by zero is not allowed')
    else:
        print('Enter valid operator')

num1 = int(input('Enter number 1: '))
num2 = int(input('Enter number 2: '))
operator = input('Enter the operator')
calc(num1,num2,operator)
