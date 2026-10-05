capA = int(input("Capacity of Jug A: "))
capB = int(input("Capacity of Jug B: "))
goal = int(input("Goal amount in Jug A: "))

a = 0
b = 0

print("\nInitial State: A =", a, "B =", b)

while a != goal:

    print("\nCurrent State: A =", a, "B =", b)

    print("\nChoose a move:")
    print("1. Fill Jug A")
    print("2. Fill Jug B")
    print("3. Empty Jug A")
    print("4. Empty Jug B")
    print("5. Pour A into B")
    print("6. Pour B into A")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        a = capA

    elif choice == 2:
        b = capB

    elif choice == 3:
        a = 0

    elif choice == 4:
        b = 0

    elif choice == 5:
        transfer = min(a, capB - b)
        a = a - transfer
        b = b + transfer

    elif choice == 6:
        transfer = min(b, capA - a)
        b = b - transfer
        a = a + transfer

    elif choice == 7:
        print("Program exited.")
        break

    else:
        print("Invalid choice!")

    if a == goal:
        print("\nGoal Reached!")
        print("Jug A =", a, "litres")
        print("Jug B =", b, "litres")
