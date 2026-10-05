from collections import deque

jug1=4
jug2=3
goal=2

def get_next_states(state):
    x,y=state
    states=[]

    states.append(((jug1,y),"fill jug1"))
    states.append(((x,jug2),"fill jug2"))
    states.append(((0,y),"empty jug1"))
    states.append(((x,0),"empty jug2"))
    amount=min(x,jug2-y)
    states.append(((x-amount,y+amount),"pour jug1 into jug2"))
    amount=min(y,jug1-x)
    states.append(((x+amount,y-amount),"pour jug2 into jug1"))

    return states

def bfs():
    initial_state=(0,0)

    queue=deque([(initial_state,[])])
    visited={initial_state}

    while queue:
        current_state,path=queue.popleft()

        x,y=current_state

        if x==goal or y==goal:
            return path+[(current_state,"goal reached")]
    
        for next_state,operation in get_next_states(current_state):
            if next_state not in visited:
                visited.add(next_state)

                new_path=path+[(current_state,operation)]
                queue.append((next_state,new_path))

    return None
    
solution=bfs()

if solution:
    print("shortest solution: ")

    for state,operation in solution:
        print(operation,"->",state)
else:
    print("no solution found")