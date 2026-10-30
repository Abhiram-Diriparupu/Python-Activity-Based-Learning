#calculating the electricity and water bill and giving message based on their usage
e = int(input("Electricity units: "))
w = int(input("Water units: "))

bill = e * 8 + w * 2

print("Total bill: Rs.", bill)

if e > 100:
    print("High electricity usage")

if w > 500:
    print("High water usage")
