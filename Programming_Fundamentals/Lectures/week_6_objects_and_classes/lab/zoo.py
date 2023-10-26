class Zoo:
    __animals = 0

    def __init__(self, name_of_zoo):
        self.name_of_zoo = name_of_zoo
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animals(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        result = ''
        if species == 'mammal':
            result += f"Mammals in {self.name_of_zoo}: {', '.join(self.mammals)}"
        elif species == 'fish':
            result += f"Fishes in {self.name_of_zoo}: {', '.join(self.fishes)}"
        elif species == 'bird':
            result += f"Birds in {self.name_of_zoo}: {', '.join(self.birds)}"
        result += f"\nTotal animals: {Zoo.__animals}"
        return result

zoo = input()
zoo_name = Zoo(zoo)
num = int(input())
for i in range(num):
    animal_type, animal = input().split()
    zoo_name.add_animals(animal_type, animal)
input_line = input()
print(zoo_name.get_info(input_line))
