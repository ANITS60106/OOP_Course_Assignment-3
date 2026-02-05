from datetime import datetime


class Amount:
    def __init__(self, amount, transaction_type):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")

        if transaction_type not in ("DEPOSIT", "WITHDRAWAL"):
            raise ValueError("Invalid transaction type.")

        self.amount = float(amount)
        self.transaction_type = transaction_type
        self.timestamp = datetime.now()

    def __str__(self):
        return f"[{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}] {self.transaction_type}: {self.amount:.2f}"


class PersonalAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount):
        transaction = Amount(amount, "DEPOSIT")
        self.transactions.append(transaction)
        self.balance += transaction.amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds.")

        transaction = Amount(amount, "WITHDRAWAL")
        self.transactions.append(transaction)
        self.balance -= transaction.amount

    def print_transaction_history(self):
        if not self.transactions:
            print("No transactions yet.")
            return

        print("\n=== Transaction History ===")
        for t in self.transactions:
            print(t)

    def get_balance(self):
        return self.balance

    def __str__(self):
        return (
            f"Account Number: {self.account_number}\n"
            f"Account Holder: {self.account_holder}\n"
            f"Balance: {self.balance:.2f}"
        )

    def __add__(self, amount):
        self.deposit(amount)
        return self

    def __sub__(self, amount):
        self.withdraw(amount)
        return self


def run_demo():
    print("=== Personal Account Management ===")

    account_number = int(input("Enter account number: "))
    account_holder = input("Enter account holder name: ")

    account = PersonalAccount(account_number, account_holder)

    while True:
        print("\n1) Deposit")
        print("2) Withdraw")
        print("3) Check Balance")
        print("4) Print Transaction History")
        print("5) Show Account Info")
        print("6) Exit")

        choice = input("Choose (1-6): ")

        try:
            if choice == "1":
                amount = float(input("Deposit amount: "))
                account.deposit(amount)
                print("Deposit successful.")

            elif choice == "2":
                amount = float(input("Withdraw amount: "))
                account.withdraw(amount)
                print("Withdrawal successful.")

            elif choice == "3":
                print(f"Current balance: {account.get_balance():.2f}")

            elif choice == "4":
                account.print_transaction_history()

            elif choice == "5":
                print(account)

            elif choice == "6":
                print("Goodbye!")
                break

            else:
                print("Invalid choice.")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    run_demo()
