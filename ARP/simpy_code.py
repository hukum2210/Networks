import simpy

def arp(env, ip):
    print(env.now, "Broadcast ARP request for", ip)
    yield env.timeout(1)
    print(env.now, "ARP reply received for", ip)

env = simpy.Environment()
env.process(arp(env, "192.168.1.2"))
env.run()
