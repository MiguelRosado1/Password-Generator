import random
import string
import time
import os

alphabet = list(string.ascii_lowercase)
alphabetHigher = list(string.ascii_uppercase)
numbers = [str(n) for n in range(10)]
symbols = ['!', '*', '@']

print("Hello and welcome to the password generator!")
print("To begin, enter what you want to do")

while True:
    choice = input("1. generate a password\n2. store a password\n3. list passwords\n4. delete password\n5. exit\n")

    if choice == '1':
        try:
            num = int(input("Enter the amount of digits you want your password to be (4 - 255): "))
        except ValueError:
            print("That's not a valid number!")
            continue
        if num < 4:
            print("It must be higher than 4!")
            continue
        elif num > 255:
            print("It must be lower than 255!")
            continue

        all_characters = alphabet + alphabetHigher + numbers + symbols
        password = random.choices(all_characters, k=num)
        password = ''.join(password)
        print(password)

        storingPassword = input(f"Do you want to store this password {password} (yes/no): ")
        if storingPassword.lower() == 'yes':
            passwordFor = input("What is this password for (e.g. Steam, Google ...): ")
            gmail = ""
            if passwordFor.lower() == 'gmail' or passwordFor.lower() == 'email':
                gmail = input("what is your gmail.com (this is run localy on your conputer so its not gonna steal your info :>)\n (leave empty if its not an email): ")
            comment = input("Any comment you want to add (leave empty for none): ")
            obj = time.localtime()
            with open("password.txt", "a") as f:
                f.write(time.asctime(obj) + " | " + "password: " + password + " | " + "from: PasswordGeneratorV2.1.45" + " | " + f"For: {passwordFor}" + " | " + f"gmail: {gmail}" + " | " + f"comment: {comment}" + '\n')

    elif choice == '2':
        storedPassword = input("What password do you want to store? (paste here the password): ")
        passwordFor = input("What is this password for (e.g. Steam, Google ...): ")
        gmail = ""
        if passwordFor.lower() == 'gmail' or passwordFor.lower() == 'email':
            gmail = input("what is your gmail.com (this is run localy on your conputer so its not gonna steal your info :>)\n (leave empty if its not an email): ")
        obj = time.localtime()
        with open("password.txt", "a") as j:
            j.write(time.asctime(obj) + " | " + "password: " + storedPassword + " | " + "from: User" + " | " + f"For: {passwordFor}" + " | " + f"gmail: {gmail}" + '\n')

    elif choice == '3':
        print("Here are the current passwords stored: \n")
        if os.path.exists("password.txt"):
            with open("password.txt") as k:
                print(k.read())
        else:
            print("No passwords stored yet.")

    elif choice == '4':
        if not os.path.exists("password.txt"):
            print("No passwords stored yet.")
            continue
        with open("password.txt") as f:
            lines = f.readlines()
        if not lines:
            print("No passwords stored yet.")
            continue
        print("Here are the current passwords stored:\n")
        for i, line in enumerate(lines):
            print(f"{i + 1}. {line.strip()}")
        try:
            toDelete = int(input("\nEnter the number of the password you want to delete: "))
        except ValueError:
            print("That's not a valid number!")
            continue
        if toDelete < 1 or toDelete > len(lines):
            print("Invalid selection!")
            continue
        del lines[toDelete - 1]
        with open("password.txt", "w") as f:
            f.writelines(lines)
        print("Password deleted.")

    elif choice == '5':
        print("Bye!!")
        break

    else:
        print("Invalid choice, please try again.\n")