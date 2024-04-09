import requests

from bs4 import BeautifulSoup
import csv
# Test de recupération d'une url d'un seul jeu
# links = []
#
# url = "https://www.philibertnet.com/fr/50-jeux-de-societe/s-3/meilleures-ventes/categorie-jeux_de_societe"
# page = requests.get(url)
#
# soup = BeautifulSoup(page.content, 'html.parser')
# anchors = soup.find_all("a", class_="product_img_link")
# for anchor in anchors:
#     link = anchor['href']
#     links.append(link)
#

# Récupération de toutes les url de jeux sur toutes les pages, plus ecriture d'un cvs
# for i in range(232):
#     url = "https://www.philibertnet.com/fr/50-jeux-de-societe/s-3/meilleures-ventes/categorie-jeux_de_societe?p=" + str(i)
#     page = requests.get(url)
#
#     soup = BeautifulSoup(page.content, 'html.parser')
# # links = soup.find_all("div", class_="wrapper_product_1")
#     anchors = soup.find_all("a", class_="product_img_link")
#     for anchor in anchors:
#         link = anchor['href']
#         links.append(link)
# # Save links to a CSV file
# with open('board_game_links.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['Link'])
#     for link in links:
#         writer.writerow([link])
#
# print("Links saved to board_game_links.csv")



# Test de recupération de donnée sur une url
# url = "https://www.philibertnet.com/fr/kyf-edition/132798-stop-me-or-let-me-go-3701252800185.html#img"
# page = requests.get(url)
#
# soup = BeautifulSoup(page.content, 'html.parser')
# image = soup.find("a", {"class": "fancybox shown"}).get("href")
# titre = soup.find("h1", id="product_name").text
# duree = soup.find("li", class_="duree_partie tooltips").text
# description = soup.find("div", id="short_description_content").text
# nb_joueur = soup.find("li", class_="nb_joueurs tooltips").text
# print(image)
# print(titre)
# print(duree)
# print(description)
# print(nb_joueur)

# Ouvrir le fichier CSV en mode écriture et créer un objet writer
with open('board_game_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Image', 'Titre', 'Durée', 'Description', 'Nombre de joueurs']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Écrire l'en-tête du fichier CSV
    writer.writeheader()

    # Liste pour stocker les URLs
    links = []

    # Lire les URLs à partir du fichier CSV
    with open('board_game_links.csv', 'r', newline='') as linkfile:
        reader = csv.reader(linkfile)
        next(reader)  # Ignorer l'en-tête
        for row in reader:
            links.append(row[0])

    # Boucle sur chaque URL
    for url in links:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        try:
            image = soup.find("a", {"class": "fancybox shown"}).get("href")
        except AttributeError:
            image = ""
        try:
            titre = soup.find("h1", id="product_name").text
        except AttributeError:
            titre = ""
        try:
            duree = soup.find("li", class_="duree_partie tooltips").text
        except AttributeError:
            duree = ""
        try:
            description = soup.find("div", id="short_description_content").text
        except AttributeError:
            description = ""
        try:
            nb_joueur = soup.find("li", class_="nb_joueurs tooltips").text
        except AttributeError:
            nb_joueur = ""

        # Écrire les données dans le fichier CSV
        writer.writerow({'Image': image, 'Titre': titre, 'Durée': duree, 'Description': description,
                         'Nombre de joueurs': nb_joueur})

print("Données enregistrées dans board_game_data.csv")