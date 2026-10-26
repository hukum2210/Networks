import socket
import threading

records = {
    "www.example.com" : "192.21.3.5" , 
    "www.openai.com" : "212.89.43.8"
}

def handle(c):
    with c :
        name = c.recv(1024).decode().strip()

        print("Recursive server " , name)
        print("Root server : finding TLD")
        print("TLD server : finding authorative server")

        ip = records.get(name , "Name not found")
        print("Authorative answer : " , ip)
        c.send(ip.encode())

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)
s.bind(("127.0.0.1" , 5006))
s.listen()
print("DNS Server ready")

while True :
    c , _ = s.accept()
    threading.Thread(target = handle , args = (c,)).start()
