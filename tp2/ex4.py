class personne:
    def __init__(self,nom,prenom,age):
        self.nom=nom
        self.prenom=prenom
        self.age=age
    def se_present(self):
        return 'my name '+self.nom+' '+self.prenom+' and i am '+str(self.age)+' years old'
class etudient(personne):
    def __init__(self, nom, prenom, age,matricule):
        super().__init__(nom, prenom, age)  
        self.matricule=matricule  
    def etudier(self):
        return self.se_present()+' and my matricule is '+self.matricule
et1=etudient("el-atiki","yassine",22,'D1234')
print(et1.etudier())