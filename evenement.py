import tkinter as tk
from threading import Thread
import time

REFRESH_MY_UI_EVENT = '<<RefreshMyUIEvent>>'

# Création de la fenêtre principale
root = tk.Tk()

def  on_long_task_completed(event):
    print('Task completed - will refresh the UI')

def long_task():
    print('Long Task starting')
    time.sleep(10)
    print('Long Task finished - pushing event for UI refresh')
    root.event_generate(REFRESH_MY_UI_EVENT, when='tail')

def on_button_click(event):

    label = event.widget.cget("text")
    print(f"Le bouton {label} a été cliqué !")
    if hasattr(event.widget, "associated_object"):
        print(f"L'objet selectionné {event.widget.associated_object}.")
    job = Thread(target=long_task)
    job.start()
    print("Fin de l'action")

def on_menu_click(widget):
    print("Click menu")

root.bind(REFRESH_MY_UI_EVENT,on_long_task_completed)

# Création d'un Frame dans la fenêtre principale
frame = tk.Frame(root)
frame.pack()

label = tk.Label(frame, text="Bonjour Tkinter !")
label.pack()

class MonCompte:
    pass
    def __str__(self):
        return "MonCompte"

mon_objet = MonCompte()

# Ajout d'un champ de saisie
entry = tk.Entry(frame)
entry.pack()

# Ajout d'un bouton
button1 = tk.Button(root, text="Bouton 1 - Cliquez-moi")
button1.bind("<Button-1>", on_button_click)
button1.associated_object = mon_objet
button1.pack()

# Ajout d'un bouton
button2 = tk.Button(root, text="Bouton 2 - Cliquez-moi")
button2.associated_object = {"key1": "value1"}
button2.bind("<Button-1>", on_button_click)
button2.bind("<Button-2>", on_button_click)
button2.pack()


# Création d'une barre de menu
menu_bar = tk.Menu(root)

# Ajout du menu à la fenêtre principale
root.config(menu=menu_bar)

# Création d'un menu déroulant
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Fichier", menu=file_menu)
file_menu.add_command(label="Nouveau", command=on_menu_click)
file_menu.add_command(label="Quitter", command=root.quit)


root.mainloop()