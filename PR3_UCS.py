import heapq

graph={
    "A":[("B",1),("D",5)],
    "B":[("A",1),("C",4),("D",3)],
    "C":[("B",4),("E",7)],
    "D":[("B",3),("A",5),("G",4),("E",1)],
    "E":[("C",7),("D",1),("G",2),("F",1)],
    "G":[("D",4),("E",2),("F",10)],
    "F":[("G",10),("E",1)],
}

def ucs(graph,start,goal):

    priority_queue=[(0,start,[start])]
    visited={}

    while priority_queue:
        cost,node,path=heapq.heappop(priority_queue)

        if node in visited and visited[node]<=cost:
            continue

        visited[node]=cost

        if node==goal:
            return path,cost

        for neighbor,edge_cost in graph[node]:
            new_cost=cost+edge_cost
            new_path=path+[neighbor]

            heapq.heappush(
                priority_queue,(new_cost,neighbor,new_path))

    return None,float("inf")
            

start="A"
goal="F"

path,cost=ucs(graph,start,goal)

print("optimal path : ","-->".join(path))
print("minimum cost : ",cost)
