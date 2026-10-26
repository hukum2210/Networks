import socket

c = socket.create_connection(('127.0.0.1' , 8001))
c.send(input("Enter the IP address : ").encode())
print(c.recv(1024).decode())
c.close()