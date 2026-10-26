import socket

table = {
    "AA:AA:AA:AA:AA:01" : "192.1.1.10" , 
    "BB:BB:BB:BB:BB:01" : "192.1.1.20"
}

s = socket.socket()
s.bind(("127.0.0.1" , 5001))
s.listen()

print("RARP server ready")

c ,_ = s.accept()

mac = c.recv(1024).decode().upper()
ip = table.get(mac , "MAC address not found")
c.send(ip.encode())

c.close()
s.close()