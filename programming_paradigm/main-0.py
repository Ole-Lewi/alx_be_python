import sys
from bank_account import BankAccount

def main():
    # Initialize the account with a starting balance of 100 (example)
    account = BankAccount(100)

    # Check if the correct number of arguments are passed
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Parse the command and parameters
    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    # Execute based on the command
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command. Use one of the following: deposit, withdraw, display.")

if __name__ == "__main__":
    main()
