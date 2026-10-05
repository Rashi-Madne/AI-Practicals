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

def