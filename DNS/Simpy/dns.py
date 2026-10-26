import simpy

records = {
    "www.example.com" : "192.21.3.5" , 
    "www.openai.com" : "212.89.43.8"
}

def dns_lookup( env , name ):
    print(f"{env.now}: Client asks for the recursive server {name}")
    yield env.timeout(1)
    print(f"{env.now}:Root server : finding TLD")
    yield env.timeout(1)
    print(f"{env.now}:TLD server : finding authorative server")
    yield env.timeout(1)
    print(f"{env.now}:IP address : {records.get(name , "Nmae not found")}")

env = simpy.Environment()
env.process(dns_lookup(env , "www.example.com"))
env.process(dns_lookup(env , "www.openai.com"))
env.run()
