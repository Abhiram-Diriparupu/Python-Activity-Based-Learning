total = int(input("Total classes: "))
attended = int(input("Attended classes: "))

if total <= 0 or attended < 0 or attended > total:
    print("Invalid input")
else:
    percentage = attended / total * 100
    print("Current attendance:", percentage, "%")

    if percentage >= 75:
        print("Attendance eligible")
    else:
        count = 0

        while (attended + count) / (total + count) < 0.75:
            count += 1

        print("Attend next", count, "classes")
        print("Attendance will reach 75%")