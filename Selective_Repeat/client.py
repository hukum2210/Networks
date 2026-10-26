import socket

n = int(input("Number of frames: "))
s = socket.socket()
s.connect(("127.0.0.1", 5005))
s.send(str(n).encode())

for i in range(n):
    print("Sending frame", i)
    s.send(str(i).encode())
    ack = s.recv(1024).decode()
    print("ACK", ack)

s.close()
