import sqlite3

def initialiser_base_de_donnees():
    conn = sqlite3.connect('comptes.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS comptes
        (numeroCompte INTEGER PRIMARY KEY, 
        nomProprietaire TEXT, 
        solde FLOAT, 
        autorisationDecouvert INTEGER, 
        pourcentageAgios FLOAT)
    ''')

    # Fermer la connexion après la création de la table
    conn.close()

def enregistrer_compte(nomProprietaire, solde, autorisationDecouvert, pourcentageAgios):
    conn = sqlite3.connect('comptes.db')
    cursor = conn.cursor()

    solde = float(solde)
    autorisationDecouvert = float(autorisationDecouvert)
    pourcentageAgios = float(pourcentageAgios)

    cursor.execute("INSERT INTO comptes (nomProprietaire, solde, autorisationDecouvert, pourcentageAgios) VALUES (?, ?, ?, ? )",
                   (nomProprietaire, solde, autorisationDecouvert, pourcentageAgios))
    conn.commit()

    # Fermer la connexion après l'enregistrement du compte
    conn.close()
