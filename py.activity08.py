n = int(input("Enter number of days: "))

for i in range(n):
    prepared = int(input("Meals prepared: "))
    served = int(input("Meals served: "))

    if prepared <= 0 or served < 0 or served > prepared:
        print("Invalid data")
    else:
        waste = prepared - served
        percentage = waste / prepared * 100

        print("Leftover:", waste)
        print("Wastage:", percentage, "%")

        if percentage > 20:
            print("High wastage")
        else:
            print("Normal wastage")