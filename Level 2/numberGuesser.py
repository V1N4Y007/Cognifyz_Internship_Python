import random
num1 = int(input('Enter number 1: '))
num2 = int(input('Enter number 2: '))
number = random.randint(num1,num2)

n = int(input('Enter the number : '))
while True:
    if n>number:
        print('too high')
        n = int(input('Enter the number : '))
    elif n<number:
        print('too low')
        n = int(input('Enter the number : '))
    else:
        print('You guessed the correct number')
        break