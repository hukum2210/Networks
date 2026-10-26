import socket

s = socket.socket()
s.bind(("0.0.0.0", 5000))
s.listen(1)
print("TCP server waiting...")

c, addr = s.accept()
print("Connected:", addr)

while True:
    msg = c.recv(1024).decode()
    if not msg or msg == "bye":
        break
    print("Client:", msg)
    reply = input("Server: ")
    c.send(reply.encode())
    if reply == "bye":
        break

c.close()
s.close()
