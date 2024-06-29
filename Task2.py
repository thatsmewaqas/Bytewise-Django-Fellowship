class Account:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Invalid or insufficient funds for withdrawal.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return (f"Account Number: {self.account_number}\n"
                f"Account Holder: {self.account_holder}\n"
                f"Balance: {self.balance}")


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        print(f"Account added: {account.account_holder} ({account.account_number})")

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def list_accounts(self):
        if not self.accounts:
            print("No accounts found.")
        for account in self.accounts:
            print(account)


def main():
    bank = Bank()

    while True:
        print("\nWelcome to the Banking System")
        print("1. Create a new account")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Check balance")
        print("5. List all accounts")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            account_number = input("Enter account number: ")
            account_holder = input("Enter account holder name: ")
            initial_balance = float(input("Enter initial balance: "))
            new_account = Account(account_number, account_holder, initial_balance)
            bank.add_account(new_account)

        elif choice == '2':
            account_number = input("Enter account number: ")
            account = bank.find_account(account_number)
            if account:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            else:
                print("Account not found.")

        elif choice == '3':
            account_number = input("Enter account number: ")
            account = bank.find_account(account_number)
            if account:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            else:
                print("Account not found.")

        elif choice == '4':
            account_number = input("Enter account number: ")
            account = bank.find_account(account_number)
            if account:
                print(f"Current balance: {account.get_balance()}")
            else:
                print("Account not found.")

        elif choice == '5':
            bank.list_accounts()

        elif choice == '6':
            print("Thank you for using the banking system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()