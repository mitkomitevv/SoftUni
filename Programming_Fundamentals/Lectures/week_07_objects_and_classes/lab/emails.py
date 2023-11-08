class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

my_list = []
command = input()
while command != 'Stop':
    sender, receiver, content = command.split()
    email = Email(sender, receiver, content)
    my_list.append(email)
    command = input()

index = [int(x) for x in input().split(', ')]

for i in index:
    my_list[i].send()

for email in my_list:
    print(email.get_info())

