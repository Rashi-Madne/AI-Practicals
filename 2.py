from collections import deque

# Jug capacities
A = 4
B = 3

# Goal check
def goal(state):
    return state[0] == 2 or state[1] == 2

def moves(state):
    a, b = state

    return [
        ((A, b), "Fill A"),
        ((a, B), "Fill B"),
        ((0, b), "Empty A"),
        ((a, 0), "Empty B"),
        ((a - min(a, B - b),
          b + min(a, B - b)), "Pour A to B"),
        ((a + min(b, A - a),
          b - min(b, A - a)), "Pour B to A")
    ]

def bfs():
    queue = deque([((0, 0), [])])
    visited = {(0, 0)}

    while queue:
        state, path = queue.popleft()

        if goal(state):
            return state, path

        for next_state, action in moves(state):

            if next_state not in visited:
                visited.add(next_state)

                queue.append((
                    next_state,
                    path + [(action, next_state)]
                ))

    return None, []

goal_state, solution = bfs()

print("Water Jug Problem using BFS")
print("Jug A = 4 litres, Jug B = 3 litres")
print("Initial State: (0, 0)")

print("\nShortest Path:")

for i, (action, state) in enumerate(solution, 1):
    print("Step", i, ":", action, "->", state)

print("\nGoal Reached!")
print("Goal State:", goal_state)
print("Total Steps:", len(solution))
