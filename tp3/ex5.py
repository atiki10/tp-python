class Employe:
    def __init__(self, nom, prenom, salaire):
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire

class Manager(Employe):
    def __init__(self, nom, prenom, salaire):
        super().__init__(nom, prenom, salaire)
        self.equipes = []

    def ajouter_emp(self, employe):
        self.equipes.append(employe)

    def afficher_emp(self):
        print(f"les employes supervisé par {self.nom} {self.prenom}")
        for emp in self.equipes:
            print(f"nom : {emp.nom}, prenom : {emp.prenom}, salaire :{emp.salaire}")

emp1 = Employe("asklo","abd",7500)
emp2 = Employe("ait mol","nordin",7800)

manager = Manager("el-atiki","yassine",10000,)
manager.ajouter_emp(emp1)
manager.ajouter_emp(emp2)
manager.afficher_emp()
