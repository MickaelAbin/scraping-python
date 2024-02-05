import sqlite3

# Connecter à SQLite
conn = sqlite3.connect('ma_base_de_donnees.db')

# Créer un objet cursor
cursor = conn.cursor()

# # Créer une table
# cursor.execute('''CREATE TABLE etudiants (
#                   id INTEGER PRIMARY KEY,
#                   nom TEXT,
#                   age INTEGER,
#                   grade TEXT)''')

# Insérer des données
cursor.execute('''INSERT INTO etudiants (nom, age, grade)
                  VALUES ('Alice', 21, 'A')''')

# Commit pour sauvegarder les changements
conn.commit()

