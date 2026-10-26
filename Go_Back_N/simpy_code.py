import simpy
import random

def sender(env):
    for i in range(5):
        print(env.now, "Send frame", i)
        yield env.timeout(1)
        if random.random() < 0.2:
            print(env.now, "Timeout: resend frame", i)
        print(env.now, "ACK", i)

env = simpy.Environment()
env.process(sender(env))
env.run()
