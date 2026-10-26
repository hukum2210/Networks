import socket
import json

HOST = "127.0.0.1"   # Replace with receiver computer's IP for Wi-Fi/LAN
PORT = 5005
TOTAL = 5
WINDOW = 3
TIMEOUT = 1.0

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(TIMEOUT)

base = 1
next_packet = 1

while base <= TOTAL:
    # Send new packets while there is room in the window.
    while next_packet < base + WINDOW and next_packet <= TOTAL:
        s.sendto(json.dumps({"packet": next_packet}).encode(), (HOST, PORT))
        print("Sent packet:", next_packet)
        next_packet += 1

    try:
        data, _ = s.recvfrom(1024)
        ack = json.loads(data.decode())["ack"]
        print("Received cumulative ACK:", ack)

        if ack >= base:
            base = ack + 1
    except socket.timeout:
        print("Timeout: retransmitting outstanding packets")
        next_packet = base

print("Transmission complete.")
s.close()
