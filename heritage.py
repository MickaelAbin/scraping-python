class Animal:
    def __init__(self, nom):
        self.nom = nom

class Aquatique:
    def plouf(self):
        return "plouf !"

class Chien(Animal):
    pass

class Chat(Animal):
    pass

class Poisson(Animal, Aquatique):
    pass

if __name__ == '__main__':
    animal1 = Chien("Rex")
    animal2 = Chat("Gaufrette")
    animal3 = Poisson("Bulle")
    print(animal3.plouf())