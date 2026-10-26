import socket

s = socket.socket()
s.bind(("0.0.0.0", 5005))
s.listen()
print("Selective Repeat server waiting...")

c, addr = s.accept()
n = int(c.recv(1024).decode())
for i in range(n):
    frame = int(c.recv(1024).decode())
    print("Received frame:", frame)
    c.send(str(frame).encode())

c.close()
s.close()
