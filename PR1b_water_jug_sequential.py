jug1=4
jug2=3

x=0
y=0

def fill_jug1():
    global x
    x=jug1
    print(x,y)

def fill_jug2():
    global y
    y=jug2
    print
    print(x,y)

def empty_jug1():
    global x
    x=0
    print(x,y)

def empty_jug2():
    global y
    y=0
    print(x,y)

def pour_jug1_into_jug2():
    global x,y
    amount=min(x,jug2-y)
    x=x-amount
    y=y+amount
    print(x,y)

def pour_jug2_into_jug1():
    global x,y
    amount=min(y,jug1-x)
    x=x+amount
    y=y-amount
    print(x,y)

print("initial states",(x,y))

fill_jug1()
pour_jug1_into_jug2()
empty_jug2()
fill_jug1()
pour_jug1_into_jug2()

print("goal state",(x,y))