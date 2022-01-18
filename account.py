
# Defining ATM menu functions. 
# These function will be called in the app.py file. 
def show_balance(balance):
    print("The current balance is: $"+str(balance))

def deposit(balance):
    amount = input("Enter amount to deposit: ")
    return balance + float(amount)

def withdraw(balance):
    amount = input("Enter amount to withdraw: ")
    if amount > balance:
        print("Where are you going to get that kind of money")
    return balance - float(amount)


def logout(name):
    print("Goodye", name + "!")
