balance = 1000

while True:
    withdrawal_amount = int(input("Enter withdrawal amount: "))
    
    if withdrawal_amount < 0:
        print("Invalid: Amount cannot be negative.")
    elif withdrawal_amount > balance:
        print("Invalid: Insufficient balance.")
    else:
        break

new_balance = balance - withdrawal_amount
print("Withdrawal successful. New balance:", new_balance)