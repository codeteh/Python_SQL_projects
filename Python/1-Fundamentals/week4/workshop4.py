class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        self.name = name

    def change_pin(self, pin):
        self.pin = pin

    def change_password(self, password):
        self.password = password


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0
    
    def show_balance(self):
        print(f"{self.name} has an account balance of: ${self.balance}")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"Withdrawn: ${amount}")
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${self.balance}")
        
    def transfer_money(self, receiving_user, amount):
        print(f"You are transferring ${amount} to {receiving_user.name}")
        if int(input("Enter your pin:")) == self.pin:
            self.withdraw(amount)
            receiving_user.deposit(amount)
            return True
        else:
            print("Invalid PIN. Transaction canceled.")
            return False

    def request_money(self, sending_user, amount):
        if int(input("Enter your pin:")) == self.pin:
            password = input("Enter password: ")
            if password == sending_user.password:
                sending_user.balance -= amount
                self.balance += amount
                print(f"You are requesting ${amount} from {sending_user.name}")
                return True
            else:
                print("Invalid password. Transaction canceled")
                return False
        else:
            print("Invalid Pin. Transaction canceled")
            return False







""" Driver Code for Task 1 
user1 = User("Bob", 1234, "password")
print(user1.name, user1.pin, user1.password) """


""" # Driver Code - Task 2
user1 = User("Bob", "1234", "password")
print(user1.name, user1.pin, user1.password)
user1.change_name('Robert')
user1.change_pin('1111')
user1.change_password('password1234')
print(user1.name, user1.pin, user1.password) """


""" Driver Code for Task 3
bankuser1 = BankUser("Bob", 1234, "password")
print(bankuser1.name, bankuser1.pin, bankuser1.password, bankuser1.balance) """

""" Driver Code for Task 4
bankuser1 = BankUser("Bob", 1234, "password")
bankuser1.show_balance()
bankuser1.deposit(1000)
bankuser1.show_balance
bankuser1.withdraw(500)
bankuser1.show_balance() """


""" Driver Code for Task 5"""
bankuser1 = BankUser("Bob", 1234, "password")
bankuser2 = BankUser("Ron", 5678, "wordpass")

bankuser2.deposit(5000)
bankuser2.show_balance()
bankuser1.show_balance()

bankuser2.transfer_money(bankuser1, 500)
bankuser2.show_balance()
bankuser1.show_balance()

if bankuser2.transfer_money(bankuser1, 500):
    bankuser2.request_money(bankuser1, 100)
bankuser1.show_balance()
bankuser2.show_balance()
