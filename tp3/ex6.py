from ex4 import Produit

class Commande:
    def __init__(self, produit, quantite):
        self.produit = produit
        self.quantite = quantite


class Panier:
    def __init__(self):
        self.commandes = []

    def ajouter_commande(self, commande):
        self.commandes.append(commande)

    def calculer_total(self):
        total = 0
        for commande in self.commandes:
            total += commande.produit.get_prix() * commande.quantite
        return total


produit1 = Produit("Produit 1", 210)
produit2 = Produit("Produit 2", 220)
produit3 = Produit("Produit 3", 250)

commande1 = Commande(produit1, 5)
commande2 = Commande(produit2, 1)
commande3 = Commande(produit3, 4)

panier = Panier()

panier.ajouter_commande(commande1)
panier.ajouter_commande(commande2)

print(f"La somme du panier est : {panier.calculer_total()} DHs")

panier.ajouter_commande(commande3)
print(f"La somme du panier apres ajout commande3 est : {panier.calculer_total()} DHs")
