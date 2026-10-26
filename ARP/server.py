import socket

table = {
    "192.168.1.1": "AA:AA:AA:AA:AA:01",
    "192.168.1.2": "AA:AA:AA:AA:AA:02",
    "192.168.1.3": "AA:AA:AA:AA:AA:03"
}

s = socket.socket()
s.bind(("0.0.0.0", 5003))
s.listen()
print("ARP server waiting...")

while True:
    c, addr = s.accept()
    ip = c.recv(1024).decode()
    mac = table.get(ip, "IP address not found")
    c.send(mac.encode())
    c.close()
