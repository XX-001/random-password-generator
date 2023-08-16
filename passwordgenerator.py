import string
import random

password_characters =list(string.ascii_letters + string.digits + "!@#$%^&*|")

def generate_password():
    password_length = int(input("How long do you want your password to be: "))

    random.shuffle(password_characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(password_characters))

    random.shuffle(password)

    password = "".join(password)

    print(password)

option = input("Do you wqnt to generate your password(Yes/No: )")

if option == "Yes" or "yes" or "YES":
    generate_password()
elif option == "No" or "NO" or "no":
    print("Program Ended")
    quit()
else:
    print("Invalid Input")
    quit()