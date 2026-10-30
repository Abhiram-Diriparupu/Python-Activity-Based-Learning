#charging parking fee according to their parking time 
hours = int(input("Enter parking hours: "))
vehicle = input("Enter bike or car: ")

if hours < 0:
    print("Invalid hours")
elif vehicle == "bike":
    fee = hours * 20
    print("Parking fee: Rs.", fee)
elif vehicle == "car":
    fee = hours * 40
    print("Parking fee: Rs.", fee)
else:
    print("Invalid vehicle")
