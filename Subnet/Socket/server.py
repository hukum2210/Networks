import socket

s = socket.socket()
s.bind(('127.0.0.1',8001))
s.listen()
print("Server is connected on the port 8001")

while True:
    c , addr = s.accept()

    p = c.recv(1024).decode().strip().split(".")

    if len(p) != 4 or not all( part.isdigit() and 0 <= int(part) <= 255 for part in p) :
        c.send("Invalid IP address".encode())

    else:
        net = '.'.join(p[:3])
        c.send(f"First usable address : {net}.1\nLast usable address : {net}.254".encode())

    c.close()