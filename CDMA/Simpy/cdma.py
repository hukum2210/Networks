import simpy

codes = {
    "A" : [ 1 , 1 , 1 , 1 ] ,
    "B" : [ 1 , -1 , 1 , -1 ]
}

def server( env , q ):
    signals = []

    for _ in range(2):
        name , bit = yield q.get()

        value = 1 if bit == "1" else -1
        signal = [ value * x for x in codes[name]]
        signals.append((name , signal))

    combined = [
                sum( sig[1][i] for sig in signals)
                for i in range(4)
            ]

    print("Combined signal : " , combined)


    for name , code in codes.items() :
        value = sum( combined[i] * code[i] for i in range(4)) / 4
        print("Recovered " , name , ":" , "1" if value > 0 else "0")

def client( env , name , bit , q ):
    print(f"{env.now}: Sending {name} with bit {bit}")
    yield q.put((name , bit ))
    print("Data sent")

env = simpy.Environment()
q = simpy.Store(env)

env.process(server( env , q ))
env.process(client( env , "A" , "0" , q))
env.process(client( env , "B" , "1" , q))

env.run()

