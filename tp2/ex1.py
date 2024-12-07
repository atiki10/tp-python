class chien:
    def __init__(self,nom,race,age):
        self.nom=nom
        self.race=race
        self.age=age
    def aboyer(self):
        return 'wooof'
ch1=chien('chien1','race1','2ans')
print(ch1.aboyer())