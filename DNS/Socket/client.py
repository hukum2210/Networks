import socket

name = input("Enter the name : ")

c = socket.create_connection(( "127.0.0.1" , 5006))
c.send(name.encode())

print("IP address : " , c.recv(1024).decode())

c.close()