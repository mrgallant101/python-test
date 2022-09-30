import datetime as dt

current_time = dt.datetime.now()
year = current_time.year
month = current_time.month
day = current_time.day
full_date = f"{day}-{month}-{year}"
print(full_date)


class BankAccount:
    def __init__(self, first_name, middle_name, last_name, account_number):
        self.balance = 0
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.account_number = account_number
        self.full_date = full_date
        print(f"Welcome {first_name} {middle_name} {last_name} with account number {account_number} to our Bank App")

    def deposit(self):
        """"A method that will make deposit"""
        amount = float(input("Enter amount you want to Deposit: "))
        self.balance += amount
        print("\nYou have deposited : $", amount)

    def withdraw(self):
        """"A method that withdraws funds from account"""
        amount = float(input("Enter amount you want to Withdraw: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\nYou Withdrew: $", amount)
        else:
            print("\nYou have insufficient balance sir ")

    def transfer_funds(self):
        """A method to transfer funds"""
        account_number = input("Enter account number to transfer funds to: ")
        amount = float(input("Enter amount you want to transfer: "))
        if len(account_number) != 10:
            print("You Entered an invalid account number: ")
        elif amount <= self.balance:
            self.balance -= amount
            print(f"You have transfer $ {amount} to {account_number} successfully ")
        else:
            print("You dont have sufficient funds to make transfer: ")

    def display(self):
        """A method to display your current balance"""
        print("\nYour available Balance = $", self.balance)

    def show_menu(self):
        """A method that will return user details and current day"""
        print(f"Thank you for banking with us\n{self.first_name} {self.middle_name} {self.last_name}\n"
              f"Your account balance is $ {self.balance}\nToday's date is {self.full_date}  ")


user = BankAccount("Sani", "Ojocheneme", "Sunday", "0053565565")

user.deposit()
user.withdraw()
user.transfer_funds()
user.display()
user.show_menu()
