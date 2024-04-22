from database import *

print(dir())

def register_customer():
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        account_number = input("Enter your account number: ")

        if validate_account_number(account_number):
           if account_number not in customers:
                customers[account_number] = {
                    'first_name': first_name,
                    'last_name': last_name
                }      
                balances[account_number]=0
                print("you have registered successfully.")
           else:
                print("Account number already exists.")
        else:
             print("Incorrect format")
        
       


def add_balance():
    account_number = input("Enter your account number for transaction money: ")
    if not validate_account_number(account_number):
        print("Invalid account number format.")
        return
    if account_number in customers:
        amount = input("Enter the amount of money you want to deposit: ")
        if amount.isdigit():
            amount = float(amount)
            balances[account_number] += amount
            print(f"Balance filled with {amount} GEL.")
        else:
            print("Invalid amount entered.")
    else:
        print("Account number does not exist.")
    

def transfer_money():
    main_account = input("Enter your account number: ")
    if not validate_account_number(main_account):
        print("Invalid account number format.")
        return
    
    if main_account in customers:
        recipient_account = input("Enter the account number you want to transfer money to: ")
        if not validate_account_number(recipient_account) or recipient_account not in customers:
            print("The account number does not exist.")
            return
        amount = input("Enter the amount of money you want to transfer: ")
        if amount.isdigit():
            amount =  float(amount)
            if balances[main_account] >= amount:
                balances[main_account] -= amount
                balances[recipient_account] +=amount
                print(f"You have successfuly transferred {amount} GEL to {customers[recipient_account]['first_name']} {customers[recipient_account]['first_name']}.")
            else:
                print("Not enough money.")
        else:
            print("Invalid money entered.")
    else:
        print("Entered (main) account number does not exist.")

if __name__ == "__main__":
        while True:
            print("Enter 1 to register: ")
            print("Enter 2 to add balance: ")
            print("Enter 3 to transfer money: ")
            choice = input("Choose an operation (1, 2 or 3): ")
            
            if choice == '1':
                register_customer()
                
            elif choice == '2':
                add_balance()
            elif choice=='3':
                transfer_money()
            else:
                print("Invalid choice")