import socket

ip = input("Enter IP address: ")
s = socket.socket()
s.connect(("127.0.0.1", 5003))
s.send(ip.encode())
print("MAC address:", s.recv(1024).decode())
s.close()
