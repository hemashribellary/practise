c_password = '123789'
attempts=0
max_attempts=3
while attempts < max_attempts:
    password = input("Enter the password: ")
    if password == c_password:
        print("Access granted.")
        break
    else:
        attempts += 1
        print(f"Incorrect password. You have {max_attempts - attempts} attempts left.")
    if attempts == max_attempts:
        print("Access denied.System locked.")
        