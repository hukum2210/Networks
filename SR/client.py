import socket
import json
import time

HOST = "127.0.0.1"   # Replace with receiver computer's IP for Wi-Fi/LAN
PORT = 5006
TOTAL = 5
WINDOW = 3
TIMEOUT = 1.0

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(0.2)

acked = set()
base = 1

while base <= TOTAL:
    end = min(base + WINDOW - 1, TOTAL)

    # Send only packets in this window that are not ACKed yet.
    for packet in range(base, end + 1):
        if packet not in acked:
            s.sendto(json.dumps({"packet": packet}).encode(), (HOST, PORT))
            print("Sent packet:", packet)

    deadline = time.time() + TIMEOUT
    while time.time() < deadline:
        try:
            data, _ = s.recvfrom(1024)
            ack = json.loads(data.decode())["ack"]
            acked.add(ack)
            print("Received individual ACK:", ack)
        except socket.timeout:
            pass

    # Slide base past all consecutively ACKed packets.
    while base in acked:
        base += 1

    if base <= TOTAL and any(p not in acked for p in range(base, end + 1)):
        print("Timeout: retransmit only unACKed packets")

print("Transmission complete.")
s.close()
