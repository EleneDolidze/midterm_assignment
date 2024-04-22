
def validate_account_number(account_number):
    if len(account_number)==5 and account_number.startswith('TB') and account_number[2:].isdigit():
        print("Correct format")
    else:
        print("Incorrect format")
     

customers = {}
balances = {}
print(dir())