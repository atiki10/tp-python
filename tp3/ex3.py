from ex1 import *
def afficher_surface(formes):
    for forme in formes:
        print(f"Surface de {forme.__class__.__name__} : {forme.calculer_surface()}")

cercle = Cercle(2)
rectangle = Rectangle(4,2)
formes = [cercle, rectangle]
afficher_surface(formes)

