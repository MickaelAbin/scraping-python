#!/usr/bin/env python3

PROMPT_BIENVENUE = \
"""Bienvenue sur l'application de la Societe Geniale
Pour quittez, appuyez sur CTRL+C"""

PROMPT_CHOIX_COMPTE = \
"""Quel compte souhaitez-vous utiliser ?
- Compte courant (1)
- Compte épargne (2)
default: Compte courant"""

PROMPT_CHOIX_OPERATION = \
"""Quelle opération souhaitez-vous effectuer ?
- Retrait (1)
- Versement (2)
- Afficher le solde (3)"""

SEPARATOR = "-"  * 20


class Compte:
    
    def __init__(self, 
                 numeroCompte, 
                 nomProprietaire, 
                 solde=0.0) -> None:
        self.numeroCompte = numeroCompte
        self.nomProprietaire = nomProprietaire
        self.solde = float(solde)

    def retrait(self, montant):
        if montant > self.solde:
            print(f"Compte: {self.numeroCompte}, Solde insuffisant")
            return None
        self.solde -= montant
        return montant

    def versement(self, montant):
        if montant < 0:
            print("Montant invalide")
            return
        self.solde += montant
    
    def afficher_solde(self):
        print(f"Compte: {self.numeroCompte}, solde: {self.solde:,.2f} euros")
    
    def __str__(self) -> str:
        return f"Compte: {self.numeroCompte}\n  Nom: {self.nomProprietaire}\n  Solde: {self.solde:,.2f} euros"


class CompteCourant(Compte):

    def __init__(self, 
                 numeroCompte, 
                 nomProprietaire, 
                 solde, 
                 autorisationDecouvert=-2000 ,
                 poucentageAgios=0.05) -> None:
        super().__init__(numeroCompte, nomProprietaire, solde)
        self.autorisationDecouvert = float(autorisationDecouvert)
        self.poucentageAgios = float(poucentageAgios)
    
    def __str__(self) -> str:
        return super().__str__() \
            + f"\n  Autorisation découvert: {self.autorisationDecouvert:,.2f} euros\n  Agios: {self.poucentageAgios:,.2f} %"
    
    def retrait(self, montant):
        agio = 0
        ancien_solde = self.solde
        self.solde -= montant
        if self.solde < self.autorisationDecouvert:
            agio = self.appliquer_agios()
        
        print(f"""Compte: {self.numeroCompte}
        Retrait demandé: {montant:,.2f} euros
        Solde avant retrait: {ancien_solde:,.2f} euros
        Solde après retrait: {self.solde:,.2f} euros
        Agios appliqué: {agio:,.2f} euros""")
    
    def versement(self, montant):
        agio = 0
        ancien_solde = self.solde
        super().versement(montant)

        if self.solde < self.autorisationDecouvert:
            agio = self.appliquer_agios()

        print(f"""Compte: {self.numeroCompte}
        Versement demandé: {montant:,.2f} euros
        Solde avant versement: {ancien_solde:,.2f} euros
        Solde après versement: {self.solde:,.2f} euros
        Agios appliqué: {agio:,.2f} euros
        """)

    def appliquer_agios(self):
        agio = abs(self.solde) * (self.poucentageAgios)
        self.solde -= agio
        return agio

class CompteEpargne(Compte):
        
    def __init__(self, numeroCompte, nomProprietaire, solde, pourcentageInteret=0.015) -> None:
        super().__init__(numeroCompte, nomProprietaire, solde)
        self.pourcentageInteret = float(pourcentageInteret)
    
    def retrait(self, montant):
        solde_initial = self.solde
        retrait = super().retrait(montant)
        interet = 0
        if retrait and retrait > 0:
            interet = self.appliquer_interets()
        print(f"""Compte: {self.numeroCompte}
        Retrait demandé: {montant:,.2f} euros
        Solde avant retrait: {solde_initial:,.2f} euros
        Solde après retrait: {self.solde:,.2f} euros
        Interets appliqués: {interet:,.2f} euros""")
    
    def versement(self, montant):
        solde_initial = self.solde
        super().versement(montant)
        interet = self.appliquer_interets()
        print(f"""Compte: {self.numeroCompte}
        Versement demandé: {montant:,.2f} euros
        Solde avant versement: {solde_initial:,.2f} euros
        Solde après versement: {self.solde:,.2f} euros
        Interets appliqués: {interet:,.2f} euros""")

    def appliquer_interets(self):
        interet = self.solde * self.pourcentageInteret
        self.solde += interet
        return interet

    def __str__(self) -> str:
        return super().__str__() \
        + f"\n  Interets: {self.pourcentageInteret:,.2f} %"


def effectuer_retrait(compte):
    print(f"vous avez choisi d'effectuer un RETRAIT sur le compte: {compte.numeroCompte}")
    montant = demanderMontant("montant du retrait:")
    compte.retrait(montant)

def effectuer_versement(compte):
    print(f"vous avez choisi d'effectuer un VERSEMENT sur le compte: {compte.numeroCompte}")
    montant = demanderMontant("montant du versement:")
    compte.versement(montant)

def afficher_solde(compte):
    compte.afficher_solde()




def demanderMontant(prompt="montant:"):
    montant = None
    while montant is None:
        try:
            montant = input(prompt)
            return float(montant)
        except ValueError:
            print("Montant invalide - eg. 18.89")
            montant = None

def parse_option(option):
    return 0 if option == "" else int(option)

def demander_option(prompt="choix:"):
    option = None
    while option is None:
        try:
            option = input(prompt)
            return parse_option(option)
        except ValueError:
            print("Option invalide - eg. 1")
            option = None


def main():
    cc = CompteCourant(123456789, "Jean", 1000)
    ce = CompteEpargne(987654321, "Jean", 2000)
    comptes = [cc, ce]
    actions = [effectuer_retrait, effectuer_versement, afficher_solde]
    
    try:
        print(PROMPT_BIENVENUE)
        while(True):
            print(PROMPT_CHOIX_COMPTE)
            option = demander_option()
            c = comptes[option - 1]
            print(f"Vous avez choisi:\n{SEPARATOR}\n{c}")
            print(PROMPT_CHOIX_OPERATION)
            option = demander_option()
            action = actions[option - 1]
            action(c)
    except KeyboardInterrupt:
        print("Au revoir")


    # Your code here

if __name__ == "__main__":
    main()