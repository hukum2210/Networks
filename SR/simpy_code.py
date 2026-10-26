import simpy

def sender(env, packets, acks, stats):
    total = 5
    window = 3
    base = 1
    acked = set()

    while base <= total:
        end = min(base + window - 1, total)

        for p in range(base, end + 1):
            if p not in acked:
                yield env.timeout(0.1)
                packets.put(p)
                stats["sent"] += 1
                print("Sending:", p)

        yield env.timeout(0.5)

        while acks.items:
            acked.add(acks.items.pop(0))

        for p in range(base, end + 1):
            if p not in acked:
                print("Retransmitting:", p)
                yield env.timeout(0.1)
                packets.put(p)
                stats["sent"] += 1

        yield env.timeout(0.5)

        while acks.items:
            acked.add(acks.items.pop(0))

        while base in acked:
            base += 1

def receiver(env, packets, acks, stats):
    lost = False
    received = set()

    while len(received) < 5:
        p = yield packets.get()
        yield env.timeout(0.1)

        if p == 2 and not lost:
            print("Packet 2 lost!")
            stats["lost"] += 1
            lost = True
            continue

        received.add(p)
        print("Received:", p)
        acks.put(p)

        stats["delivered"] = len(received)

env = simpy.Environment()
packets = simpy.Store(env)
acks = simpy.Store(env)

stats = {"sent": 0, "lost": 0, "delivered": 0}
packet_size = 1000

env.process(sender(env, packets, acks, stats))
env.process(receiver(env, packets, acks, stats))
env.run()

elapsed = env.now
loss = stats["lost"] / stats["sent"] * 100
throughput = stats["delivered"] * packet_size / elapsed

print("\nTransmissions:", stats["sent"])
print("Lost packets:", stats["lost"])
print("Delivered packets:", stats["delivered"])
print("Packet loss:", round(loss, 2), "%")
print("Throughput:", round(throughput, 2), "bits/sec")
