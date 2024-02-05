import time
import tkinter as tk

# Création de la fenêtre principale
root = tk.Tk()
def on_menu_click():
    print("Le menu a été cliqué !")

# Création d'un Frame dans la fenêtre principale
frame = tk.Frame(root)
frame.pack()
# Création d'une barre de menu
menu_bar = tk.Menu(root)

# Ajout du menu à la fenêtre principale
root.config(menu=menu_bar)

# Création d'un menu déroulant
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Fichier", menu=file_menu)
file_menu.add_command(label="Nouveau", command=on_menu_click)
file_menu.add_command(label="Quitter", command=root.quit)
# Ajout d'une étiquette
label = tk.Label(frame, text="Bonjour Tkinter !")
label.pack()

# Ajout d'un champ de saisie
entry = tk.Entry(frame)
entry.pack()

# Ajout d'un bouton
def on_button_click():
    print("Le bouton a été cliqué !")


button = tk.Button(root, text="Cliquez-moi", command=on_button_click)
button.pack()

# time.sleep(10)

def on_menu_click():
    print("Le menu a été cliqué !")

root.mainloop()
