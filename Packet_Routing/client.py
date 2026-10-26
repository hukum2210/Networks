import socket

start = input("Source node (A-D): ").upper()
end = input("Destination node (A-D): ").upper()

s = socket.socket()
s.connect(("127.0.0.1", 5007))
s.send((start + " " + end).encode())
print("Shortest route:", s.recv(1024).decode())
s.close()
