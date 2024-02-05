

import tkinter as tk
from exercice5 import initialiser_base_de_donnees, enregistrer_compte

# Initialiser la base de données
initialiser_base_de_donnees()
def creer_compte():
    nomProprietaire = nomProprietaire_entry.get()
    solde = solde_entry.get()
    autorisationDecouvert = autorisationDecouvert_entry.get()
    pourcentageAgios = pourcentageAgios_entry.get()

    # Call the renamed function from exercice5.py to create an account in the database
    enregistrer_compte(nomProprietaire, solde, autorisationDecouvert, pourcentageAgios)

# Créer la fenêtre principale
root = tk.Tk()
root.title("Création de comptes")
# root.config(background="red")
root.geometry("300x300")

nomProprietaire = tk.StringVar()
solde= tk.StringVar()
autorisationDecouvert= tk.StringVar()
pourcentageAgios= tk.StringVar()


# Créer une frame
frame = tk.Frame(root)
# frame.config(background="yellow")
# Créer un Label avec le texte "Création de comptes" et des options de personnalisation
label = tk.Label(frame, text="Création de comptes", font=("Arial", 20),  anchor="w")

# Ajouter le Label à la frame
label.pack(side=tk.LEFT, padx=10, pady=5)

# Ajouter la frame à la fenêtre à gauche et la remplir horizontalement
frame.pack(side=tk.TOP, fill=tk.BOTH)

# Créer une deuxième frame
formulaire = tk.Frame(root)
formulaire.pack(padx=10, pady=10, fill='x', expand=True)

# nom
nomProprietaire_label = tk.Label(formulaire, text="Nom:")
nomProprietaire_label.pack(fill='x', expand=True)

nomProprietaire_entry = tk.Entry(formulaire, textvariable=nomProprietaire)
nomProprietaire_entry.pack(fill='x', expand=True)
nomProprietaire_entry.focus()

# solde
solde_label = tk.Label(formulaire, text="solde:")
solde_label.pack(fill='x', expand=True)

solde_entry = tk.Entry(formulaire, textvariable=solde)
solde_entry.pack(fill='x', expand=True)


# autorisationDecouvert
autorisationDecouvert_label = tk.Label(formulaire, text="autorisationDecouvert:")
autorisationDecouvert_label.pack(fill='x', expand=True)

autorisationDecouvert_entry = tk.Entry(formulaire, textvariable=autorisationDecouvert)
autorisationDecouvert_entry.pack(fill='x', expand=True)

# pourcentageAgios
pourcentageAgios_label = tk.Label(formulaire, text="pourcentageAgios:")
pourcentageAgios_label.pack(fill='x', expand=True)

pourcentageAgios_entry = tk.Entry(formulaire, textvariable=pourcentageAgios)
pourcentageAgios_entry.pack(fill='x', expand=True)

# Bouton pour déclencher la création du compte
enregistrement_button = tk.Button(formulaire, text="Enregistrer", command=creer_compte)
enregistrement_button.pack(fill='x', expand=True, pady=10)






# Lancer la boucle principale
root.mainloop()

