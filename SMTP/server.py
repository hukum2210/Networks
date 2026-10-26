import pickle

user = input("Username: ")
password = input("Password: ")

if password == "123":
    print("Authentication successful!")

    emails = pickle.load(open("mail.txt", "rb"))
    print("Total messages:", len(emails))

    n = int(input("Enter message number: "))
    e = emails[n-1]

    print("Sender:", e[0])
    print("Recipient:", e[1])
    print("Subject:", e[2])
    print("Message:", e[3])
else:
    print("Authentication failed!")