import simpy

def sender(env):
    for i in range(1, 6):
        print(env.now, "Sending packet", i)
        yield env.timeout(1)
        print(env.now, "Packet", i, "received")

env = simpy.Environment()
env.process(sender(env))
env.run()
