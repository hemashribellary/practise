print('do you want odd or even numbers within a range of natural numbers?')
choice = input("Type 'odd' or 'even': ")
if choice == 'odd':
    n = int(input("Enter the range of natural numbers: "))
    for i in range(1, n + 1, 2):
        print(i)
elif choice == 'even':
    n = int(input("Enter the range of natural numbers: "))
    for i in range(2, n + 1, 2):
        print(i)