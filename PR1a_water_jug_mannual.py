jug1=4
jug2=3

jug=int(input("jug with goal amount(1/2): "))
amt=int(input("goal amount: "))

x=0
y=0
print("initial states are",(x,y))

while True:
    print("choose an operation : ")
    print("1. fill jug1")
    print("2. fill jug2")
    print("3. empty jug1")
    print("4. empty jug2")
    print("5. pour jug1 into jug2")
    print("6. pour jug2 into jug1")
    print("7. exit")

    choice=int(input("enter your choice: "))

    if choice==1:
        x=jug1

    elif choice==2:
        y=jug2

    elif choice==3:
        x=0

    elif choice==4:
        y=0

    elif choice==5:
        amount=min(x,jug2-y)
        x=x-amount
        y=y+amount

    elif choice==6:
        amount=min(y,jug1-x)
        x=x+amount
        y=y-amount

    elif choice==7:
        break

    else:
        print("invalid choice")
        continue

    print("current state : ",(x,y))

    if  (jug==1 and x==amt) or (jug==2 or y==amt):
        print("goal reached")
        break

