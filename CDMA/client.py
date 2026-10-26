import socket

name = input("Enter name (A/B) : ")
bit = input("Enter the data bit (0/1) : ")

c = socket.create_connection(("127.0.0.1" , 5002))
c.send(f"{name} {bit}".encode())
c.close()

print("Data sent")
