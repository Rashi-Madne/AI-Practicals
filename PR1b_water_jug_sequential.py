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
    print(x,y)

def empty_jug1():
    global x
    x=0
    print(x,y)

def empty_jug2():
    global y
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
    y=y-amount
    x=x+amount
    print(x,y)

print("initial state ",(x,y))

fill_jug1()
fill_jug2()
pour_jug1_into_jug2()
pour_jug2_into_jug1()
empty_jug1()
empty_jug2()

print("goal state",(x,y))