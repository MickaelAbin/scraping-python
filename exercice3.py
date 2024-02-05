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
        

class CompteCourant(Compte) :
    def __init__(self, numeroCompte, nomProprietaire, solde,autorisationDecouvert,pourcentageAgios):
        super().__init__(numeroCompte, nomProprietaire, solde)
        self.autorisationDecouvert = autorisationDecouvert
        self.pourcentageAgios = pourcentageAgios



    def calculAgios(self):
        if self.solde < 0-self.autorisationDecouvert:
             montant = (abs(self.solde)-self.autorisationDecouvert)*(self.pourcentageAgios/100)
             return montant
        else:
            return 0
        
    def retrait(self,montant):
        super().retrait(montant)
        self.solde=self.solde - self.calculAgios()
        return self.solde

    def versement(self,versement):
        super().versement(versement)
        return self.solde


class CompteEpargne(Compte):
    def __init__(self, numeroCompte, nomProprietaire, solde,pourcentageInterets):
        super().__init__(numeroCompte, nomProprietaire, solde)
        self.pourcentageInterets = pourcentageInterets

   
 
    def retrait(self,montant):
        super().retrait(montant)
        self.solde = self.calculInteret()
        return self.solde

    def versement(self,versement):
        super().versement(versement)
        self.solde = self.calculInteret()
        return self.solde

    def calculInteret (self):
        self.solde=self.solde+(self.solde*self.pourcentageInterets/100)
        return self.solde


# c1 = CompteCourant(123,"abin",500,100,2)

# c3=CompteEpargne(124,"abin",1000,5)

# print("entrez 1 pour contre courant ou 2 pour compte epargne")
# compte = int(input())
# if compte == 1 :
#         print(f"vous avez selectionner votre compte courant et votre solde est de {c1.solde} euros")
#         print("Entrez le montant de la transaction (positif pour un versement, négatif pour un retrait)")
#         montant = int(input())
#         if montant<0:
#             print(f"vous avez choisi un retrait de {abs(montant)} euros")
#             print(f"Votre nouveau solde est de {c1.retrait(abs(montant))} euros")
#         else:
#             print(f"Vous avez choisi un versement de {montant} euros")
#             print(f"Votre nouveau solde est de {c1.versement(montant)} euros")
# else:
#         print(f"vous avez selectionner votre compte epargne et votre solde est de {c3.solde} euros")
#         print("Entrez le montant de la transaction (positif pour un versement, négatif pour un retrait)")
#         montant = int(input())
#         if montant<0:
#             print(f"vous avez choisi un retrait de {abs(montant)} euros")
#             print(f"Votre nouveau solde est de {c3.retrait(abs(montant))} euros")
#         else:
#             print(f"Vous avez choisi un versement de {montant} euros")
#             print(f"Votre nouveau solde est de {c3.versement(montant)} euros")