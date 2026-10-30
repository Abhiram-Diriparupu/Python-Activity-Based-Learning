#assigning delivery charges based on their needs 
weight = int(input("Enter weight in kg: "))
urgent = input("Urgent delivery? yes/no: ")
restricted = input("Restricted parcel? yes/no: ")

if weight <= 0:
    print("Invalid weight")
elif restricted == "yes":
    print("Standard delivery")
    print("Charge: Rs. 50")
elif urgent == "yes":
    print("Express delivery")
    print("Charge: Rs. 100")
else:
    print("Standard delivery")
    print("Charge: Rs. 50")
