class Produit:
    def __init__(self, nom, prix):
        self.__nom = nom
        self.__prix = prix

    def get_nom(self):
        return self.__nom
    
    def set_nom(self,nom):
        self.__nom=nom

    def get_prix(self):
        return self.__prix
    
    def set_prix(self,prix):
        self.__prix=prix

    def calculer_prix_avec_remise(self, pourcentage):
        if self.__prix > 100:
            self.__prix = self.__prix - self.__prix*(pourcentage / 100)

produit = Produit("Produit 1",250)
print(f"Produit : {produit.get_nom()}")
print(f"Prix de base : {produit.get_prix()} DHs")
produit.calculer_prix_avec_remise(20)
print(f"Prix après remise : {produit.get_prix()} DHs")
