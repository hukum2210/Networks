import simpy

def client(env, name):
    for i in range(3):
        yield env.timeout(1)
        print(env.now, name, "sends message", i + 1)

env = simpy.Environment()
for i in range(3):
    env.process(client(env, "Client" + str(i + 1)))
env.run()
