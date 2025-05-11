number = int(input("Enter the number of terms: "))

n1 = 0
n2 = 1
count = 0

if number <= 0:
    print("Please enter a positive integer.")
elif number == 1:
    print(n1)
else:
    while count < number:
        print(n1, end=" ")
        sum = n1 + n2
        n1 = n2
        n2 = sum
        count += 1
