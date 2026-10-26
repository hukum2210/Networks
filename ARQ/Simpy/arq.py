import simpy

def receiver( env , q , ack_q):
    expected = 0

    while True :
        msg = yield q.get()

        if not msg or msg == "END" :
            break

        seq , data = msg
        seq = int(seq)

        if seq == expected :
            print(f"{env.now}: Received : " , data)
            yield ack_q.put(f"ACK{seq}")       
            expected = 1 - expected

        else:
            yield ack_q.put(f"ACK{1 - expected} send again")

def sender( env , ack_q , q , frames ):
    seq = 0 

    for data in frames:
        print(f"{env.now}: Sending frame {seq} : {data}")
        yield q.put((seq , data))

        ack = yield ack_q.get()
        print(f"{env.now}: Sent frame {seq} Received {ack}")

        if ack == f"ACK{seq}":
            seq = 1 - seq

    yield q.put("END")

env = simpy.Environment()
q = simpy.Store(env)
ack_q = simpy.Store(env)

env.process(receiver(env , q , ack_q ))
env.process(sender(env , ack_q , q , ["Hello" , "Computer" , "Networks"]))
env.run()

