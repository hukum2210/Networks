import socket

c = socket.create_connection(("127.0.0.1" , 5002))
seq = 0 

for data in ["Hello" , "Computer" , "Networks"]:
    c.send(f"{seq}|{data}".encode())

    ack = c.recv(1024).decode()
    print(f"Sent frame {seq} Received {ack}")

    if ack == f"ACK{seq}":
        seq = 1 - seq

c.send("END".encode())
c.close()