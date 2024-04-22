class BankAccount:
    def __init__(self, name, account_number, account_type, initial_balance):
        self.name = name
        self.account_number = account_number
        self.account_type = account_type
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited RS.{amount}. New balance is Rs.{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew Rs.{amount}. New balance is Rs.{self.balance}")
        else:
            print("Insufficient funds!")

    def display_details(self):
        print(f"Account Details\nName: {self.name}\nAccount Number: {self.account_number}\nAccount Type: {self.account_type}\nBalance: Rs.{self.balance}")

name = input("Enter your name: ")
account_number = input("Enter your account number: ")
account_type = input("Enter account type: ")
initial_balance = float(input("Enter initial balance: "))

account = BankAccount(name, account_number, account_type, initial_balance)
account.display_details()

while True:
    print("Choose an action:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        deposit_amount = float(input("Enter amount to deposit: "))
        account.deposit(deposit_amount)
    elif choice == '2':
        withdraw_amount = float(input("Enter amount to withdraw: "))
        account.withdraw(withdraw_amount)
    elif choice == '3':
        break
    else:
        print("Invalid choice!!")

    account.display_details()
