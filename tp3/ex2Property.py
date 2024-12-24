class Personne:
    def __init__(self, nom, prenom, age):
        self.__nom = nom
        self.__prenom = prenom
        self.__age = age

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        if isinstance(value, str):
            self.__nom = value
 
    @property
    def prenom(self):
        return self.__prenom

    @prenom.setter
    def prenom(self, value):
        if isinstance(value, str):
            self.__prenom = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if isinstance(value, int) and value > 0:
            self.__age = value

pr=Personne("atiki","yassine",22)
print(f"nom : {pr.nom} , prenom : {pr.prenom} , age : {pr.age}")
pr.nom="el-atiki"
print(f"nom : {pr.nom} , prenom : {pr.prenom} , age : {pr.age}")
