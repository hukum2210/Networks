import simpy
import random

def node(env, name):
    for i in range(3):
        yield env.timeout(random.randint(1, 3))
        print(env.now, name, "sending packet")

env = simpy.Environment()

for i in range(3):
    env.process(node(env, "Node" + str(i + 1)))

env.run()
