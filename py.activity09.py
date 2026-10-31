stock = [10, 10]
price = [20, 40]
total = 0

n = int(input("Number of orders: "))

for i in range(n):
    choice = int(input("1.Idli  2.Dosa: "))
    qty = int(input("Enter quantity: "))

    if choice < 1 or choice > 2 or qty <= 0:
        print("Invalid order")
    elif qty > stock[choice-1]:
        print("Stock unavailable")
    else:
        bill = qty * price[choice-1]
        stock[choice-1] -= qty
        total += bill
        print("Bill:", bill)

print("Total sales:", total)
print("Remaining stock:", stock)