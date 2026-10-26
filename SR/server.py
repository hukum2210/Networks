import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("127.0.0.1", 5006))

total = 5
received = set()
lost = False
lost_count = 0

while len(received) < total:
    data, addr = s.recvfrom(1024)
    msg = data.decode()

    if msg == "STATS":
        s.sendto(f"{lost_count},{len(received)}".encode(), addr)
        continue

    p = int(msg)
    print("Received:", p)

    if p == 2 and not lost:
        print("Packet 2 lost!")
        lost = True
        lost_count += 1
        continue

    received.add(p)
    s.sendto(str(p).encode(), addr)
    print("ACK sent:", p)

while True:
    data, addr = s.recvfrom(1024)

    if data.decode() == "STATS":
        s.sendto(f"{lost_count},{len(received)}".encode(), addr)
        break

s.close()
