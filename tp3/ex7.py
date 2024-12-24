from abc import ABC, abstractmethod

class Vehicule(ABC):
    @abstractmethod
    def deplacer(self):
        pass

class Voiture(Vehicule):
    def deplacer(self):
        print("voiture")

class Bicyclette(Vehicule):
    def deplacer(self):
        print("bicyclette")
