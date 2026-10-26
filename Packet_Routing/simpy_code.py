import simpy

def packet(env, path):
    for i in range(len(path) - 1):
        print(env.now, "Packet moves", path[i], "to", path[i + 1])
        yield env.timeout(1)
    print(env.now, "Packet arrived at", path[-1])

env = simpy.Environment()
env.process(packet(env, ["A", "B", "C", "D"]))
env.run()
