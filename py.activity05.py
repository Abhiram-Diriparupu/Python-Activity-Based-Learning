# calculating railway fare and reservation 
n = int(input("Number of passengers: "))
distance = int(input("Distance in km: "))
total = 0

for i in range(n):
    age = int(input("Enter passenger age: "))
    cls = input("Enter class (sleeper/ac): ")

    fare = distance * 2

    if cls == "ac":
        fare = fare * 2

    if age < 5:
        fare = 0
    elif age >= 60:
        fare = fare * 0.8

    if fare > 0:
        fare = fare + 20

    print("Passenger fare: Rs.", fare)
    total = total + fare

print("Total fare: Rs.", total)