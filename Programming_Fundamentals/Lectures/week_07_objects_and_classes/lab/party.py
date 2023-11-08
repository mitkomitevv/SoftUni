class Party:
    def __init__(self):
        self.people = []

party = Party()
names = input()
while names != 'End':
    party.people.append(names)

    names = input()
print(f"Going: {', '.join(party.people)}\n"
      f"Total: {len(party.people)}")
