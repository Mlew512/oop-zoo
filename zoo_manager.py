from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name: str , species: str):
        self.name = name
        self.species = species

    @abstractmethod
    def speak(self):
        pass
