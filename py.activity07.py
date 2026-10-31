balance = 5000

n = int(input("Number of transactions: "))

for i in range(n):
    choice = input("Deposit or withdraw: ")
    amount = int(input("Enter amount: "))

    if amount <= 0:
        print("Invalid amount")
    elif choice == "deposit":
        balance += amount
    elif choice == "withdraw":
        if amount > 2000:
            print("Limit exceeded")
        elif amount > balance:
            print("Insufficient balance")
        else:
            balance -= amount
    else:
        print("Invalid transaction")

print("Final balance:", balance)