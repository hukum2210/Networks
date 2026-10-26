import socket

n = int(input("Number of frames: "))
s = socket.socket()
s.connect(("127.0.0.1", 5004))
s.send(str(n).encode())

for i in range(n):
    print("Sending frame", i)
    s.send(str(i).encode())

print(s.recv(1024).decode())
s.close()
