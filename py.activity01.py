#assigning points to the sports team depending on the match result 
a = int(input("Team A score: "))
b = int(input("Team B score: "))

if a > b:
    print("Team A wins")
    print("Team A points: 3")
    print("Team B points: 0")
elif b > a:
    print("Team B wins")
    print("Team A points: 0")
    print("Team B points: 3")
else:
    print("Match Draw")
    print("Both teams get 1 point")
