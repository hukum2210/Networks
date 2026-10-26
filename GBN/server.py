import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("127.0.0.1", 5005))

expected = 1
lost = False
lost_count = 0
delivered = 0

while expected <= 5:
    data, addr = s.recvfrom(1024)
    p = int(data.decode())
    print("Received:", p)

    if p == 2 and not lost:
        print("Packet 2 lost!")
        lost = True
        lost_count += 1
    elif p == expected:
        print("Accepted:", p)
        expected += 1
        delivered += 1
    else:
        print("Discarded:", p)

    s.sendto(str(expected - 1).encode(), addr)

data, addr = s.recvfrom(1024)

if data.decode() == "STATS":
    result = f"{lost_count},{delivered}"
    s.sendto(result.encode(), addr)

s.close()
