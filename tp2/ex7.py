class Livre:
    def __init__(self, titre, auteur, annee_pub):
        self.titre = titre
        self.auteur = auteur
        self.annee_pub = annee_pub
class Bibliotheque:
    def __init__(self):
        self.livres = []
    def ajouter_livre(self, livre):
        self.livres.append(livre)
    def aff_livres(self):
        for livre in self.livres:
            print(f"titre = {livre.titre}, auteur = {livre.auteur}, annee_pub = {livre.annee_pub}")
        
biblio = Bibliotheque()
livre1 = Livre("hello", "atiki", 1999)
livre2 = Livre("slam", "yassine", 2000)
biblio.ajouter_livre(livre1)
biblio.ajouter_livre(livre2)
biblio.aff_livres()