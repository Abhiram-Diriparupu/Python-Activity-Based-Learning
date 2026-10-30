#bus passenger occupancy 
passengers = 0
capacity = 50

stops = int(input("Enter number of stops: "))

for i in range(stops):
    print("Stop", i + 1)

    board = int(input("Passengers boarding: "))
    leave = int(input("Passengers getting off: "))

    if board < 0 or leave < 0 or leave > passengers:
        print("Invalid passenger count")
    else:
        passengers = passengers - leave + board

        print("Passengers in bus:", passengers)

        if passengers > capacity:
            print("Capacity exceeded!")
        else:
            print("Capacity is OK")
