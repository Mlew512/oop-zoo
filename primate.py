from mammal import Mammal

class Primate(Mammal):
    def __init__(self, name: str, species: str):
        super().__init__(name, species)

    def climbs_trees(self):
        print(f"{self.name} is climbing trees")

        