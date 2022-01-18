from banking_pkg import account


# ATM menu function
def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


# User reguistration and balance initialization
print("          === Automated Teller Machine ===          \n")

name = input("Enter name to register: ")
while True:
    len(name) > 1 and len(name) < 10

    if len(name) <= 1:
        print("You must enter a name")
        break

    if len(name) >= 10:
        print("Maximun name length is 10 characters")
        break
    else:
        continue

pin = input("Enter pin: ")

balance = 0
print(name, "has been registered with a starting balance of", str(balance))

# User login validation
while True:
    print("")
    print("          === Automated Teller Machine ===        ")
    print("LOGIN")

    name_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter PIN: ")
    if name == name_to_validate and pin == pin_to_validate:
        print("Login succesfully")
        break
    else:
        print("Invalid credential")
        continue

# User ATM option selction
while True:
    atm_menu(name)
    option = input("Choose an option: ")

    if option == "1":
        account.show_balance(balance)
        continue

    elif option == "2":
        balance = account.deposit(balance)
        print("Current Balance: $" + str(balance))
        continue

    elif option == "3":
        balance = account.withdraw(balance)
        print("Current Balance: $" + str(balance))
        continue

    elif option == "4":
        account.logout(name)
        break

    else:
        print("Invalid selection")
        continue
