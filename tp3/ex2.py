class Personne:
    def __init__(self, nom, prenom, age):
        self.__nom = nom
        self.__prenom = prenom
        self.__age = age

    def get_nom(self):
        return self.__nom

    def set_nom(self, nom):
        if isinstance(nom, str):
            self.__nom = nom

    def get_prenom(self):
        return self.__prenom

    def set_prenom(self, prenom):
        if isinstance(prenom, str):
            self.__prenom = prenom

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if isinstance(age, int) and age > 0:
            self.__age = age
    

pr=Personne("atiki","yassine",22)
print(f"nom : {pr.get_nom()} , prenom : {pr.get_prenom()} , age : {pr.get_age()}")
pr.set_nom("el-atiki")
print(f"nom : {pr.get_nom()} , prenom : {pr.get_prenom()} , age : {pr.get_age()}")