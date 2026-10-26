import socket

c = socket.create_connection(("127.0.0.1" , 5001))
mac = input("Enter the MAC address : ")
c.send(mac.encode())

print("IP address:", c.recv(1024).decode())

c.close()