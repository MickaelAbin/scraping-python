



def calcul_prix_TTC(prixHT,pourcentage):
    prixHT = float(prixHT)
    pourcentage = float(pourcentage)
    return (prixHT-(prixHT*(pourcentage/100)))
  

if __name__ == "__main__":

        print("entrez un prix HT")
        prixHT = float(input())
        print("entrez un pourcentage de reduction")
        pourcentage_reduction = float(input())

        prixTTC=calcul_prix_TTC(prixHT,pourcentage_reduction)

        print(prixTTC)