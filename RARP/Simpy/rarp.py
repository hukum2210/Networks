import simpy

table = {
    "AA:AA:AA:AA:AA:01" : "192.1.1.20" , 
    "BB:BB:BB:BB:BB:01" : "192.1.1.10"
}

def rarp( env , mac ):
    print("RARP request for : " , mac)
    yield env.timeout(1)
    print("IP address : " , table.get(mac , "MAC not supported"))

env = simpy.Environment()
env.process(rarp( env , "AA:AA:AA:AA:AA:01"))
env.run()