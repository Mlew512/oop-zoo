from zoo_manager import Animal

class Bird(Animal):
    def __init__(self, name: str, species: str, wingspan: int):
        super().__init__(name, species)
        self.wingspan = wingspan
        