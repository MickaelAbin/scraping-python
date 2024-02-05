class Compte :
    def __init__(self,numeroCompte, nomProprietaire, solde) :
        self.numeroCompte = numeroCompte
        self.nomProprietaire = nomProprietaire
        self.solde = solde

    def retrait(self,montant):
        self.solde =  self.solde - montant

    def versement(self,versement):
        self.solde = self.solde + versement

    def afficher_solde(self):
        return print(self.solde)
        
class CompteEpargne(Compte):
    def __init__(self, numeroCompte, nomProprietaire, solde, pourcentageInterets):
        super().__init__(numeroCompte, nomProprietaire, solde)
        self.pourcentageInterets = pourcentageInterets

    def get_pourcentageInterets(self):
        return self.pourcentageInterets

    def set_pourcentageInterets(self, value):
        self.pourcentageInterets = value

    def retrait(self,montant):
        super().retrait(montant)

    def versement(self,versement):
        super().versement(versement)

    def calculInteret (self):
        self.solde=self.solde+(self.solde*self.pourcentageInterets/100)

    
c3=CompteEpargne(124,"abin",1000,5)

c4=CompteEpargne(1553,"abin",1000,6)


    