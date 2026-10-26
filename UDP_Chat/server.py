import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", 5001))
print("UDP server waiting...")

while True:
    data, addr = s.recvfrom(1024)
    msg = data.decode()
    print("Client:", msg)
    reply = input("Server: ")
    s.sendto(reply.encode(), addr)
    if msg == "bye":
        break

s.close()
