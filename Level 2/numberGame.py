import random
number = random.randint(1,100)
n = int(input('Enter the number : '))
count = 0
while True:
    count = count + 1
    if n>number:
        print('too high')
        n = int(input('Enter the number : '))
    elif n<number:
        print('too low')
        n = int(input('Enter the number : '))
    else:
        print(f'You guessed the correct number in {count} attempts')
        break