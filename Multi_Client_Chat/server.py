import socket
import threading

clients = []

def handle(c):
    while True:
        try:
            msg = c.recv(1024)
            if not msg:
                break
            for client in clients:
                if client != c:
                    client.send(msg)
        except:
            break
    clients.remove(c)
    c.close()

s = socket.socket()
s.bind(("0.0.0.0", 5002))
s.listen()
print("Multi-client server waiting...")

while True:
    c, addr = s.accept()
    clients.append(c)
    threading.Thread(target=handle, args=(c,), daemon=True).start()
