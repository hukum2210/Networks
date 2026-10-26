import simpy

def client(env, mailbox):
    print(env.now, "Client: HELO client")
    yield env.timeout(1)

    email = ["alice@example.com", "bob@example.com", "Meeting", "Hello, let's meet tomorrow!"]
    print(env.now, "Client: Sending email from", email[0], "to", email[1])
    yield env.timeout(1)

    yield mailbox.put(email)
    print(env.now, "Client: Email sent and stored!")

def server(env, mailbox):
    yield env.timeout(1)
    password = "123"
    if password == "123":
        print(env.now, "Server: Authentication successful!")
        email = yield mailbox.get()
        print(env.now, "Server: Total messages: 1")
        print("Sender:", email[0])
        print("Recipient:", email[1])
        print("Subject:", email[2])
        print("Message:", email[3])
    else:
        print(env.now, "Server: Authentication failed!")

env = simpy.Environment()
mailbox = simpy.Store(env)
env.process(client(env, mailbox))
env.process(server(env, mailbox))
env.run()
