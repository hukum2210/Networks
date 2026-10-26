import simpy

TOTAL = 5
WINDOW = 3

def sender(env, channel, acks, stats):
    acked = set()
    base = 1

    while base <= TOTAL:
        end = min(base + WINDOW - 1, TOTAL)

        # Send only unacknowledged packets in the current window.
        for packet in range(base, end + 1):
            if packet not in acked:
                print(f"{env.now}: Send packet {packet}")
                stats["sent"] += 1
                yield channel.put(packet)

        yield env.timeout(1)

        while acks.items:
            ack = yield acks.get()
            acked.add(ack)
            print(f"{env.now}: Individual ACK {ack}")

        while base in acked:
            base += 1

        if base <= TOTAL:
            missing = [p for p in range(base, end + 1) if p not in acked]
            if missing:
                print(f"{env.now}: Timeout, resend only {missing}")

def receiver(env, channel, acks, stats):
    received = set()
    dropped_packet_2 = False

    while len(received) < TOTAL:
        packet = yield channel.get()

        if packet == 2 and not dropped_packet_2:
            dropped_packet_2 = True
            stats["lost"] += 1
            print(f"{env.now}: Simulated loss of packet 2")
            continue

        if packet not in received:
            received.add(packet)
            stats["delivered"] += 1
            print(f"{env.now}: Receiver buffered packet {packet}")

        yield acks.put(packet)

def run():
    env = simpy.Environment()
    channel = simpy.Store(env)
    acks = simpy.Store(env)
    stats = {"sent": 0, "lost": 0, "delivered": 0}

    env.process(sender(env, channel, acks, stats))
    env.process(receiver(env, channel, acks, stats))
    env.run(until=20)
    print("Stats:", stats)

if __name__ == "__main__":
    run()
