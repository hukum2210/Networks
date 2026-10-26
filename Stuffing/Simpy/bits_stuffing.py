import simpy

def stuff(bits):
    out , count = "" , 0

    for b in bits :
        out += b

        if b == "1" :
            count += 1
            if count == 5 :
                out += "0"
                count = 0
        else:
            count = 0

    return out

def destuff(bits):
    out , count , i = "" , 0 , 0

    while i < len(bits) :
        b = bits[i]

        if b == "1" :
            out += b
            count += 1
            if count == 5 :
                if i+1 < len(bits) and bits[i+1] == "0" :
                    i += 1
                count = 0
        else:
            out += b
            count = 0

        i += 1

    return out

def run(env):
    bits = "0111110011111000"
    print("Original data : " + bits)

    yield env.timeout(1)
    framed = stuff(bits)
    print("Stuffed data : " + framed)

    yield env.timeout(1)
    print("Stuffed data : " + destuff(framed))

env = simpy.Environment()
env.process(run(env))
env.run()

            