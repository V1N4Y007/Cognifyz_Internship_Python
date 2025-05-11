import random
number = random.randint(1,100)
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