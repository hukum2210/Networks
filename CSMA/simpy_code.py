import simpy
import random

def channel(env, stations):
    for slot in range(10):
        yield env.timeout(1)
        active = [i for i in range(stations) if random.random() < 0.3]
        if len(active) == 0:
            print(env.now, "Idle")
        elif len(active) == 1:
            print(env.now, "Success:", active[0])
        else:
            print(env.now, "Collision:", active)

env = simpy.Environment()
env.process(channel(env, 5))
env.run()
