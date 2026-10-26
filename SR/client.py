import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(0.5)

server = ("127.0.0.1", 5006)
total = 5
window = 3
base = 1
acked = set()
sent = 0
packet_size = 1000

start = time.time()

while base <= total:
    end = min(base + window - 1, total)

    for p in range(base, end + 1):
        if p not in acked:
            s.sendto(str(p).encode(), server)
            sent += 1
            print("Sending:", p)

    while True:
        try:
            data, _ = s.recvfrom(1024)
            acked.add(int(data.decode()))

            if all(p in acked for p in range(base, end + 1)):
                break

        except socket.timeout:
            break

    for p in range(base, end + 1):
        if p not in acked:
            print("Retransmitting:", p)
            s.sendto(str(p).encode(), server)
            sent += 1

    while True:
        try:
            data, _ = s.recvfrom(1024)
            acked.add(int(data.decode()))

            if all(p in acked for p in range(base, end + 1)):
                break

        except socket.timeout:
            break

    while base in acked:
        base += 1

s.sendto(b"STATS", server)
data, _ = s.recvfrom(1024)
lost, delivered = map(int, data.decode().split(","))

elapsed = time.time() - start
loss = lost / sent * 100
throughput = delivered * packet_size / elapsed

print("\nTransmissions:", sent)
print("Packets lost:", lost)
print("Packets delivered:", delivered)
print("Packet loss:", round(loss, 2), "%")
print("Throughput:", round(throughput, 2), "bits/sec")

s.close()
