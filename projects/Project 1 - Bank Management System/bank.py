from database import Database

class BankAccount:
    # Represents a single bank account using encapsulation.
    
    def __init__(self, account_number, customer_name, balance=0.0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.__balance = balance  # Private attribute (Encapsulation)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds!")
        self.__balance -= amount
        return self.__balance

    def get_balance(self):
        """Getter for the private balance attribute."""
        return self.__balance


class BankManager:
    # Manages bank operations and interacts with the database.
    
    def __init__(self):
        self.db = Database()

    def create_account(self, acc_num, name, initial_deposit):
        if initial_deposit < 0:
            print("Initial deposit cannot be negative.")
            return

        # Check if account already exists
        if self.db.fetch_one("SELECT account_number FROM accounts WHERE account_number=?", (acc_num,)):
            print("Error: Account number already exists. Please use a unique number.")
            return

        # Insert into database
        query = "INSERT INTO accounts (account_number, customer_name, balance) VALUES (?, ?, ?)"
        if self.db.execute_query(query, (acc_num, name, initial_deposit)):
            print(f"Success! Account created for {name}.")

    def deposit_money(self, acc_num, amount):
        record = self.db.fetch_one("SELECT customer_name, balance FROM accounts WHERE account_number=?", (acc_num,))
        if not record:
            print("Error: Account not found.")
            return

        name, balance = record
        account = BankAccount(acc_num, name, balance)
        
        try:
            new_balance = account.deposit(amount)
            self.db.execute_query("UPDATE accounts SET balance=? WHERE account_number=?", (new_balance, acc_num))
            print(f"Deposited successfully. New balance: ${new_balance:.2f}")
        except ValueError as e:
            print(f"Error: {e}")

    def withdraw_money(self, acc_num, amount):
        record = self.db.fetch_one("SELECT customer_name, balance FROM accounts WHERE account_number=?", (acc_num,))
        if not record:
            print("Error: Account not found.")
            return

        name, balance = record
        account = BankAccount(acc_num, name, balance)
        
        try:
            new_balance = account.withdraw(amount)
            self.db.execute_query("UPDATE accounts SET balance=? WHERE account_number=?", (new_balance, acc_num))
            print(f"Withdrawn successfully. New balance: ${new_balance:.2f}")
        except ValueError as e:
            print(f"Error: {e}")

    def check_balance(self, acc_num):
        record = self.db.fetch_one("SELECT customer_name, balance FROM accounts WHERE account_number=?", (acc_num,))
        if record:
            print(f"Account: {acc_num} | Name: {record[0]} | Balance: ${record[1]:.2f}")
        else:
            print("Error: Account not found.")

    def view_all_accounts(self):
        records = self.db.fetch_all("SELECT account_number, customer_name, balance FROM accounts")
        if not records:
            print("No accounts found in the bank.")
            return
        
        print("\n--- All Accounts ---")
        for rec in records:
            print(f"Acc No: {rec[0]} | Name: {rec[1]} | Balance: ${rec[2]:.2f}")
        print("--------------------")

    def delete_account(self, acc_num):
        record = self.db.fetch_one("SELECT account_number FROM accounts WHERE account_number=?", (acc_num,))
        if not record:
            print("Error: Account not found.")
            return
            
        if self.db.execute_query("DELETE FROM accounts WHERE account_number=?", (acc_num,)):
            print(f"Account {acc_num} has been successfully deleted.")