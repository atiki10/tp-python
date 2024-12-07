class animal:
    def __init__(self):
        pass
    def faire_bruit(self):
        return 'bruit'
class chein(animal):
    def __init__(self):
        super().__init__()
    def faire_bruit(self):
        return super().faire_bruit()+'chain'
class chat(animal):
    def __init__(self):
        super().__init__()
    def faire_bruit(self):
        return super().faire_bruit()+'chat'
animal1=animal()
print(animal1.faire_bruit())
chein1=chein()
print(chein1.faire_bruit())
chat1=chat()
print(chat1.faire_bruit())