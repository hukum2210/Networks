import socket
import json

HOST = "0.0.0.0"
PORT = 5005
TOTAL = 5

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))
print("GBN receiver ready on port", PORT)

expected = 1
dropped_packet_2 = False

while expected <= TOTAL:
    data, addr = s.recvfrom(1024)
    msg = json.loads(data.decode())
    packet = msg["packet"]

    # Simulate losing packet 2 once.
    if packet == 2 and not dropped_packet_2:
        dropped_packet_2 = True
        print("Simulated loss: packet", packet)
        continue

    if packet == expected:
        print("Received packet:", packet)
        expected += 1
    else:
        print("Discarded out-of-order packet:", packet)

    # GBN uses cumulative ACKs.
    ack = expected - 1
    s.sendto(json.dumps({"ack": ack}).encode(), addr)
    print("Sent cumulative ACK:", ack)

print("All packets received.")
s.close()
