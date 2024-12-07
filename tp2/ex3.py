class comptebancaire:
    def __init__(self,titulaire,solde):
        self.titulaire=titulaire
        self.solde=solde
    def deposer(self,montant):
        self.solde+=montant
    def retirer(self,montant):
        if self.solde>=montant:
            self.solde-=montant
        else:
            print("solde est insuffisant")
    def aff_solde(self):
        return 'solde = '+str(self.solde)
cmp1=comptebancaire("yassine",2000)
print(cmp1.aff_solde())
cmp1.deposer(2000)
print(cmp1.aff_solde())
cmp1.retirer(2500)
print(cmp1.aff_solde())
cmp1.retirer(2000)