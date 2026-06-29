n= int(input('enter a positive integer: '))
original = n
reverse = 0
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
print(f"The reverse of {original} is {reverse}")