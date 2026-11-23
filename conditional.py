
print("Welcome to ATM")

balance = 10000

amount = int(input("Enter withdrawal amount: "))

if amount <= 0:
    print("Please enter a valid amount")

elif amount > balance:
    print("Insufficient Balance")

else:
    balance = balance - amount
    print("Withdrawal Successful!")
    print("Remaining Balance:", balance)

print("Thank you for using ATM")
