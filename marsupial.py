from mammal import Mammal

class Marsupial(Mammal):
    def __init__(self, name: str, species: str):
        super().__init__(name, species)

    def carry_baby(self):
        print(f"{self.name} is carring its baby")
    