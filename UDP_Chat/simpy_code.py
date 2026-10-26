import simpy
import random

def sender(env):
    for i in range(1, 6):
        yield env.timeout(1)
        if random.random() < 0.2:
            print(env.now, "Packet", i, "lost")
        else:
            print(env.now, "Packet", i, "received")

env = simpy.Environment()
env.process(sender(env))
env.run()
