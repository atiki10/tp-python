class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.amis = []
    def ajouter_ami(self, ami):
        self.amis.append(ami)
    def aff_amis(self):
        print("Liste d'amis:")
        for ami in self.amis:
            print(f"prenom = {ami.prenom} , nom ={ami.nom} , age ={ami.age}")

personne = Personne("atiki", "yassine", 22)
ami = Personne("ait", "nordin", 22)
ami2 = Personne("asklo","abd",23)
personne.ajouter_ami(ami)
personne.ajouter_ami(ami2)
personne.aff_amis()