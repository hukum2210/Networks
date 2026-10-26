import socket

s = socket.socket()
s.connect(("127.0.0.1", 5000))

while True:
    msg = input("You: ")
    s.send(msg.encode())
    if msg == "bye":
        break
    reply = s.recv(1024).decode()
    print("Server:", reply)
    if reply == "bye":
        break

s.close()
