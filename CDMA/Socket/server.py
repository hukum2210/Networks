import socket

codes = {
    "A" : [ 1 , 1 , 1 , 1 ] ,
    "B" : [ 1 , -1 , 1 , -1 ]
}

s = socket.socket()
s.bind(("127.0.0.1" , 5002))
s.listen()
print("Server is ready ; Waiting for two clients")

signals = []

for _ in range(2):
    c , _ = s.accept()
    name , bit = c.recv(1024).decode().split()

    value = 1 if bit == "1" else -1
    signal = [ value * x for x in codes[name]]
    signals.append((name , signal))
    c.close()

combined = [
        sum( sig[1][i] for sig in signals)
        for i in range(4)
    ]

print("Combined signal : " , combined)


for name , code in codes.items() :
    value = sum( combined[i] * code[i] for i in range(4)) / 4
    print("Recovered " , name , ":" , "1" if value > 0 else "0")

s.close()
