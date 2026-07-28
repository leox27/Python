import sys
from bank import BankManager

def show_menu():
    print()
    print("=========================")
    print("  BANK MANAGEMENT SYSTEM  ")
    print("=========================")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. View All Accounts")
    print("6. Delete Account")
    print("7. Exit")
    print("=========================")

def main():
    manager = BankManager()

    while True:
        show_menu()
        choice = input("Enter your choice (from 1 to 7): ")

        try:
            if choice == '1':
                acc_num = input("Enter Account Number: ").strip()
                name = input("Enter Customer Name: ").strip()
                deposit = float(input("Enter Initial Deposit: "))
                manager.create_account(acc_num, name, deposit)

            elif choice == '2':
                acc_num = input("Enter Account Number: ").strip()
                amount = float(input("Enter Deposit Amount: "))
                manager.deposit_money(acc_num, amount)

            elif choice == '3':
                acc_num = input("Enter Account Number: ").strip()
                amount = float(input("Enter Withdrawal Amount: "))
                manager.withdraw_money(acc_num, amount)

            elif choice == '4':
                acc_num = input("Enter Account Number: ").strip()
                manager.check_balance(acc_num)

            elif choice == '5':
                manager.view_all_accounts()

            elif choice == '6':
                acc_num = input("Enter Account Number to Delete: ").strip()
                manager.delete_account(acc_num)

            elif choice == '7':
                print("Thank you for using the Bank Management System. Goodbye!")
                sys.exit()

            else:
                print("Invalid choice. Please select a number from 1 to 7.")

        except ValueError:
            print("Invalid input...! 🤦‍♂️ Please enter correct numeric values 🤗🤗🤗")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()