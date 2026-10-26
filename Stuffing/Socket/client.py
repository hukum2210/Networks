import socket

c = socket.create_connection(('127.0.0.1' , 5001))
bits = input("Enter the bits : ")
c.send(bits.encode())

print(c.recv(1024).decode())

c.close()