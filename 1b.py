capA = int(input("Capacity of Jug A: "))
capB = int(input("Capacity of Jug B: "))
goal = int(input("Goal amount in Jug A: "))

a = 0
b = 0

def fill_A():
    global a
    a = capA

def fill_B():
    global b
    b = capB

def empty_A():
    global a
    a = 0

def empty_B():
    global b
    b = 0

def pour_A_to_B():
    global a, b
    transfer = min(a, capB - b)
    a -= transfer
    b += transfer

def pour_B_to_A():
    global a, b
    transfer = min(b, capA - a)
    b -= transfer
    a += transfer

print("\nInitial State:", a, b)

while a != goal:

    fill_B()
    print("Fill B:", a, b)

    pour_B_to_A()
    print("Pour B -> A:", a, b)

    fill_B()
    print("Fill B:", a, b)

    pour_B_to_A()
    print("Pour B -> A:", a, b)

    empty_A()
    print("Empty A:", a, b)

    pour_B_to_A()
    print("Pour B -> A:", a, b)

print("\nGoal Reached!")
print("Jug A =", a, "litres")
print("Jug B =", b, "litres")
