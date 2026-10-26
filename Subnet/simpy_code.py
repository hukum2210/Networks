import simpy

def client( env , name , ip , start , q):
    yield env.timeout(start)
    print(f"[{env.now:.1f}s] {name} sends {ip}")
    q.put((name , ip))

def server( env , q ):
    while True:
        name , ip = yield q.get()
        yield env.timeout(0.5)
        net = '.'.join(ip.split('.')[:3])
        print(f"[{env.now:.1f}s] Server -> {name}: 1st {net}.1 last {net}.254")

env = simpy.Environment()
q = simpy.Store(env)

env.process(server( env , q ))

for i , ( ip , t ) in enumerate([
    ("192.28.0.0" , 0),
    ("174.14.8.43" , 1),
    ("10.8.92.34" , 1),
] , 1 ):
    env.process(client( env , f"Client{i}" , ip , t , q))

env.run(until=10)
