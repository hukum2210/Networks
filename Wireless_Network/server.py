import socket

s = socket.socket()
s.bind(("0.0.0.0", 5010))
s.listen(5)
print("Wireless chat server started")

while True:
    client, address = s.accept()
    print("Connected:", address)
    msg = client.recv(1024).decode()
    print("Client:", msg)
    reply = input("Server reply: ")
    client.send(reply.encode())
    client.close()
