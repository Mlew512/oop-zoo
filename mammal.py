from zoo_manager import Animal

class Mammal(Animal):
    def __init__(self, name: str, species: str):
        super().__init__(name, species)

    def give_birth(self):
        print(f"{self.name} has given birth")
