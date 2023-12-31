from banking_pkg import account


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


print("          === Automated Teller Machine ===          ")
name = input("Enter Name To Register: ")
pin = input("Enter PIN: ")
balance = 0
print(f"{name} has been registered with a starting balance of ${balance}")


while True:
    print("          === Automated Teller Machine ===          ")
    print("LOGIN")
    name_to_validate = input("Enter Name: ")
    pin_to_validate = input("Enter PIN: ")

    if name_to_validate == name and pin_to_validate == pin:
        print("Login Successful")
        break
    else:
        print("Invalid Credential. Try Again.")


while True:
    atm_menu(name)
    option = input("Choose an option: ")
    if option == "1":
        balance = account.show_balance(balance)

    elif option == "2":
        balance = account.deposit(balance)
        print(f"Current Balance: {balance}")

    elif option == "3":
        balance = account.withdraw(balance)
        print(f"Current Balance: {balance}")

    elif option == "4":
        account.logout(name)
        break

    else:
        continue
