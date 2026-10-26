import socket

s = socket.socket()
s.bind(("0.0.0.0", 5004))
s.listen()
print("Go-Back-N server waiting...")

c, addr = s.accept()
n = int(c.recv(1024).decode())
expected = 0

while expected < n:
    frame = int(c.recv(1024).decode())
    print("Received frame:", frame)
    if frame == expected:
        print("ACK", frame)
        expected += 1
    else:
        print("Expected frame", expected, "- send ACK", expected - 1)

c.send(b"All frames received")
c.close()
s.close()
