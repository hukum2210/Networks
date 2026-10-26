import socket
import threading

def receive(s):
    while True:
        try:
            msg = s.recv(1024).decode()
            if not msg:
                break
            print("\nMessage:", msg)
        except:
            break

s = socket.socket()
s.connect(("127.0.0.1", 5002))
threading.Thread(target=receive, args=(s,), daemon=True).start()

while True:
    msg = input("You: ")
    if msg == "bye":
        break
    s.send(msg.encode())

s.close()
