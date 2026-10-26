import socket

stations = input("Number of stations: ")
s = socket.socket()
s.connect(("127.0.0.1", 5006))
s.send(stations.encode())

for i in range(10):
    print(s.recv(1024).decode().strip())

s.close()
