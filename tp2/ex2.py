class voiture:
    def __init__(self,marque,modele,annee):
        self.marque=marque
        self.modele=modele
        self.annee=annee
    def aff_info(self):
        return 'marque = '+ self.marque +' modele = '+self.modele+' annee = '+self.annee
v1=voiture('v1','v1999','1999')
v2=voiture('v2','v2000','2000')
v3=voiture('v3','v2010','2010')
print(v1.aff_info())
print(v2.aff_info())
print(v3.aff_info())