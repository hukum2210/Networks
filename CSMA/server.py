import socket
import random

s = socket.socket()
s.bind(("0.0.0.0", 5006))
s.listen()
print("CSMA server waiting...")

c, addr = s.accept()
stations = int(c.recv(1024).decode())

for slot in range(10):
    active = [i for i in range(stations) if random.random() < 0.3]
    if len(active) == 0:
        result = "Idle slot"
    elif len(active) == 1:
        result = "Station " + str(active[0]) + " transmitted"
    else:
        result = "Collision between stations " + str(active)
    print(result)
    c.send((result + "\n").encode())

c.close()
s.close()
