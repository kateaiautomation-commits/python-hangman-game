def is_valid_account_number(account_number):
    if len(account_number) == 6 and account_number.isdigit():
        return True
    else:
        return False


def get_account_number():
    while True:
        account_number = input("Enter your 6-digit account number: ")
        if is_valid_account_number(account_number):
            return account_number
        else:
            print("Invalid account number. Please enter exactly 6 digits.")


# Main program
valid_account_number = get_account_number()
print("Account number accepted:", valid_account_number)