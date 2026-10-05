import heapq

graph = {
    'Arad': [('Zerind', 75), ('Timisoara', 118), ('Sibiu', 140)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Drobeta', 120), ('Rimnicu Vilcea', 146),
                ('Pitesti', 138)],
    'Sibiu': [('Arad', 140), ('Oradea', 151),
              ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146),
                       ('Pitesti', 97)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138),
                ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101)]
}

heuristic = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Drobeta': 242,
    'Eforie': 161,
    'Fagaras': 176,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 100,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}


def a_star(graph, heuristic, start, goal):

    priority_queue = [
        (heuristic[start], 0, start, [start])
    ]

    visited = {}

    while priority_queue:

        f, g, city, path = heapq.heappop(priority_queue)

        if city in visited and visited[city] <= g:
            continue

        visited[city] = g

        if city == goal:
            return path, g

        for neighbor, cost in graph[city]:

            new_g = g + cost
            new_f = new_g + heuristic[neighbor]

            new_path = path + [neighbor]

            heapq.heappush(
                priority_queue,
                (new_f, new_g, neighbor, new_path)
            )

    return None, float('inf')

start = 'Arad'
goal = 'Bucharest'

path, cost = a_star(graph, heuristic, start, goal)

print("Optimal Path:", " -> ".join(path))
print("Minimum Cost:", cost)