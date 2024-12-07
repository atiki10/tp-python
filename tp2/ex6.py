class rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def calc_surface(self):
        return 'surface = '+str(self.largeur * self.hauteur)

    def calc_perimetre(self):
        return 'perimetre = '+str(2 * (self.largeur + self.hauteur))
rectangle = rectangle(4, 2)
print(rectangle.calc_surface())
print(rectangle.calc_perimetre())