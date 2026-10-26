import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server = ("127.0.0.1", 5005)

total = 5
window = 3
base = 1
sent = 0
packet_size = 1000

start = time.time()

while base <= total:
    end = min(base + window - 1, total)

    for p in range(base, end + 1):
        s.sendto(str(p).encode(), server)
        sent += 1
        print("Sending:", p)

    acks = []
    for _ in range(base, end + 1):
        data, _ = s.recvfrom(1024)
        acks.append(int(data.decode()))

    highest = max(acks)

    if highest < end:
        print("Retransmitting from:", highest + 1)

        for p in range(highest + 1, end + 1):
            s.sendto(str(p).encode(), server)
            sent += 1
            print("Retransmitting:", p)

        acks = []
        for _ in range(highest + 1, end + 1):
            data, _ = s.recvfrom(1024)
            acks.append(int(data.decode()))

        highest = max(acks)

    base = highest + 1

s.sendto(b"STATS", server)
data, _ = s.recvfrom(1024)

lost, delivered = map(int, data.decode().split(","))
elapsed = time.time() - start

loss = lost / sent * 100
throughput = delivered * packet_size / elapsed

print("\nTotal transmissions:", sent)
print("Packets lost:", lost)
print("Packets delivered:", delivered)
print("Packet loss:", round(loss, 2), "%")
print("Time:", round(elapsed, 2), "seconds")
print("Throughput:", round(throughput, 2), "bits/sec")

s.close()
