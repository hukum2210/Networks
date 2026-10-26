import socket

graph = {
    "A": {"B": 1, "C": 4},
    "B": {"A": 1, "C": 2, "D": 5},
    "C": {"A": 4, "B": 2, "D": 1},
    "D": {"B": 5, "C": 1}
}

def route(start, end):
    distance = {node: 999 for node in graph}
    previous = {}
    distance[start] = 0
    unseen = list(graph)

    while unseen:
        current = min(unseen, key=lambda node: distance[node])
        unseen.remove(current)
        for neighbor, cost in graph[current].items():
            new_cost = distance[current] + cost
            if new_cost < distance[neighbor]:
                distance[neighbor] = new_cost
                previous[neighbor] = current

    path = [end]
    while path[-1] != start:
        if path[-1] not in previous:
            return "No route found"
        path.append(previous[path[-1]])
    path.reverse()
    return " -> ".join(path) + ", cost = " + str(distance[end])

s = socket.socket()
s.bind(("0.0.0.0", 5007))
s.listen()
print("Routing server waiting...")

while True:
    c, addr = s.accept()
    data = c.recv(1024).decode().split()
    start, end = data[0], data[1]
    c.send(route(start, end).encode())
    c.close()
