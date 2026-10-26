import socket
import json

HOST = "0.0.0.0"
PORT = 5006
TOTAL = 5

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))
print("Selective Repeat receiver ready on port", PORT)

received = set()
dropped_packet_2 = False
buffer = {}

while len(received) < TOTAL:
    data, addr = s.recvfrom(1024)
    msg = json.loads(data.decode())
    packet = msg["packet"]

    # Simulate losing packet 2 once.
    if packet == 2 and not dropped_packet_2:
        dropped_packet_2 = True
        print("Simulated loss: packet", packet)
        continue

    if 1 <= packet <= TOTAL:
        if packet not in received:
            received.add(packet)
            buffer[packet] = True
            print("Buffered packet:", packet)

        # SR sends an individual ACK for each received packet.
        s.sendto(json.dumps({"ack": packet}).encode(), addr)
        print("Sent ACK:", packet)

print("Delivered in order:", list(range(1, TOTAL + 1)))
s.close()
