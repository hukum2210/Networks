import pickle

print("HELO client")

sender = input("Sender: ")
receiver = input("Recipient: ")
subject = input("Subject: ")
body = input("Message body: ")

email = [sender, receiver, subject, body]

emails = []
emails.append(email)

pickle.dump(emails, open("mail.txt", "wb"))
print("Email sent and stored!")