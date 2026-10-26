import socket

def stuff(bits):
    out , count = "" , 0

    for b in bits:
        out += b

        if b == "1" :
            count += 1
            if count == 5 :
                out += "0"
                count = 0
        else:
            count = 0

    return out

s = socket.socket()
s.bind(('127.0.0.1' , 5001))
s.listen()
print("Bit stuffing code is generated")
c , _ = s.accept()

bits = c.recv(1024).decode()
result = "Stuffed : " + stuff(bits)
c.send(result.encode())

c.close()
s.close()