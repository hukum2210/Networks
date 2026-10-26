import socket

s = socket.socket()
s.bind(("127.0.0.1" , 5002))
s.listen()
print("Server is started")
c , _ = s.accept()

expected = 0

while True :
    msg = c.recv(1024).decode()

    if not msg or msg == "END" :
        break

    seq , data = msg.split("|")
    seq = int(seq)

    if seq == expected :
        print("Received : " , data)
        c.send(f"ACK{seq}".encode())        
        expected = 1 - expected

    else:
        c.send(f"ACK{1 - expected} send again".encode())

c.close()
s.close()
