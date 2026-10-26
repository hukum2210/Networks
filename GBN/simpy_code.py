import simpy

TOTAL = 5
WINDOW = 3

def sender(env, channel, acks, stats):
    base = 1
    next_packet = 1

    while base <= TOTAL:
        # Send new packets while the window has space.
        while next_packet < base + WINDOW and next_packet <= TOTAL:
            print(f"{env.now}: Send packet {next_packet}")
            stats["sent"] += 1
            yield channel.put(next_packet)
            next_packet += 1

        yield env.timeout(1)

        received_acks = []
        while acks.items:
            received_acks.append((yield acks.get()))

        if received_acks:
            ack = max(received_acks)
            print(f"{env.now}: Cumulative ACK {ack}")
            if ack >= base:
                base = ack + 1
        else:
            print(f"{env.now}: Timeout, retransmit outstanding packets")
            next_packet = base

def receiver(env, channel, acks, stats):
    expected = 1
    dropped_packet_2 = False

    while expected <= TOTAL:
        packet = yield channel.get()

        if packet == 2 and not dropped_packet_2:
            dropped_packet_2 = True
            stats["lost"] += 1
            print(f"{env.now}: Simulated loss of packet 2")
            continue

        if packet == expected:
            print(f"{env.now}: Receiver got packet {packet}")
            stats["delivered"] += 1
            expected += 1
        else:
            print(f"{env.now}: Discard out-of-order packet {packet}")

        yield acks.put(expected - 1)

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
