import simpy

def sender(env, packets, acks, stats):
    total = 5
    window = 3
    base = 1

    while base <= total:
        end = min(base + window - 1, total)

        for p in range(base, end + 1):
            yield env.timeout(0.1)
            stats["sent"] += 1
            packets.put(p)
            print("Sending:", p)

        yield env.timeout(0.5)

        received = []
        while acks.items:
            received.append(acks.items.pop(0))

        highest = max(received, default=base - 1)

        if highest < end:
            print("Retransmitting from:", highest + 1)

            for p in range(highest + 1, end + 1):
                yield env.timeout(0.1)
                stats["sent"] += 1
                packets.put(p)
                print("Retransmitting:", p)

            yield env.timeout(0.5)

            received = []
            while acks.items:
                received.append(acks.items.pop(0))

            highest = max(received, default=base - 1)

        base = highest + 1

def receiver(env, packets, acks, stats):
    expected = 1
    lost = False

    while expected <= 5:
        p = yield packets.get()
        yield env.timeout(0.1)

        if p == 2 and not lost:
            print("Packet 2 lost!")
            stats["lost"] += 1
            lost = True

        elif p == expected:
            print("Received:", p)
            expected += 1
            stats["delivered"] += 1

        else:
            print("Discarded:", p)

        if not (p == 2 and lost and expected == 2):
            acks.put(expected - 1)

env = simpy.Environment()
packets = simpy.Store(env)
acks = simpy.Store(env)

stats = {"sent": 0, "lost": 0, "delivered": 0}
packet_size = 1000

env.process(sender(env, packets, acks, stats))
env.process(receiver(env, packets, acks, stats))
env.run()

time = env.now
loss = stats["lost"] / stats["sent"] * 100
throughput = stats["delivered"] * packet_size / time

print("\nTotal transmissions:", stats["sent"])
print("Packets lost:", stats["lost"])
print("Packets delivered:", stats["delivered"])
print("Packet loss:", round(loss, 2), "%")
print("Time:", round(time, 2), "seconds")
print("Throughput:", round(throughput, 2), "bits/sec")
