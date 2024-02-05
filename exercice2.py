def diviseur(nombre):
    i = 2
    liste = []
    while i <= nombre:
        if nombre % i == 0:
            liste.append(i)
        i += 1
    return liste

if __name__ == "__main__":
    print("Entrez un nombre entier supérieur à 1")
    nombre = int(input())
    liste = diviseur(nombre)
    if len(liste) == 1:
        print("PREMIER")
    else:
        print(liste)
