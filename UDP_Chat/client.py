import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server = ("127.0.0.1", 5001)

while True:
    msg = input("You: ")
    s.sendto(msg.encode(), server)
    if msg == "bye":
        break
    data, addr = s.recvfrom(1024)
    print("Server:", data.decode())
    if data.decode() == "bye":
        break

s.close()
