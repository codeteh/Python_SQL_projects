
def show_balance(balance):
    balance = float(balance)
    print(balance)


def deposit(balance):
    amount = input("Enter amount to deposit: ")
    amount = float(amount)
    return float(balance + amount)


def withdraw(balance):
    amount = input("Enter amount to withdraw: ")
    amount = float(amount)
    return float(balance - amount)


def logout(name):
    print(f"Goodbye {name}!")
