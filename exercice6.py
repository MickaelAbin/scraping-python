import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
from exercice4 import CompteCourant, CompteEpargne
from enum import Enum
from datetime import datetime

DEFAULT_WINDOW_GEOMETRY = "800x600+100+100"

TITLE_FONT = ("Inter", 42, "bold")
LABEL_TITLE_FONT = ("Helvetica", 12, "bold")
LABEL_VALUE_FONT = ("Helvetica", 12)


class Padding(Enum):
    TINY = 4
    SMALL = 8
    MEDIUM = 16
    LARGE = 32
    HUGE = 64


class CompteCourantBinding:
    def __init__(self, compte_courant: CompteCourant, master=None):
        self.compte_courant = compte_courant
        self._numero_compte = StringVar(master, value=self.compte_courant.numeroCompte, name="numero_compte")
        self._solde = StringVar(master, value=self.compte_courant.solde, name="solde")
        self._autorisation_decouvert = StringVar(master, value=self.compte_courant.autorisationDecouvert,
                                                 name="autorisation_decouvert")
        self._poucentage_agios = StringVar(master, value=self.compte_courant.poucentageAgios, name="poucentage_agios")
        self._nom_proprietaire = StringVar(master, value=self.compte_courant.nomProprietaire, name="nom_proprietaire")

    def update(self):
        self._numero_compte.set(self.compte_courant.numeroCompte)
        self._solde.set(self.compte_courant.solde)
        self._autorisation_decouvert.set(self.compte_courant.autorisationDecouvert)
        self._poucentage_agios.set(self.compte_courant.poucentageAgios)
        self._nom_proprietaire.set(self.compte_courant.nomProprietaire)

    @property
    def numero_compte(self):
        return self._numero_compte

    @property
    def solde(self):
        return self._solde

    @property
    def autorisation_decouvert(self):
        return self._autorisation_decouvert

    @property
    def poucentage_agios(self):
        return self._poucentage_agios

    @property
    def nom_proprietaire(self):
        return self._nom_proprietaire


class State:
    def __init__(self):
        self.compteCourant = CompteCourant(12778388389, "Jean Bernard", 1000)
        self.compteEpargne = CompteEpargne(22234564444, "Jean Bernard", 1000)


class AccoutnTypeFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.pack()
        self.create_widgets()

    def create_widgets(self):
        pass


class KeyValueFrame(tk.Frame):
    def __init__(self, master=None, key=None, value=None):
        super().__init__(master)
        self.master = master
        self.key = key
        self.value = value

        self.pack(fill=tk.X, expand=False)
        self.create_widgets()

    def create_widgets(self):
        self.key_label = tk.Label(self, text=self.key, font=LABEL_TITLE_FONT)
        self.key_label.pack(side=tk.LEFT, padx=Padding.MEDIUM.value, pady=Padding.TINY.value)
        self.value_label = tk.Label(self, textvariable=self.value, font=LABEL_VALUE_FONT)
        self.value_label.pack(side=tk.RIGHT, padx=Padding.MEDIUM.value, pady=Padding.TINY.value)


class AccountInfoFrame(tk.Frame):
    def __init__(self, binding: CompteCourantBinding, master=None):
        super().__init__(master)
        self.master = master
        self.binding = binding

        # self.config(background="pink")

        self.pack(side=tk.TOP, fill=tk.X, expand=False)
        self.create_widgets()

    def create_widgets(self):
        self.left_frame = tk.Frame(self)
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y)

        # display a simple key value pair as 2 labels
        self.kv_account = KeyValueFrame(master=self.left_frame, key="Numéro de compte:",
                                        value=self.binding.numero_compte)
        self.kv_solde = KeyValueFrame(master=self.left_frame, key="Solde:", value=self.binding.solde)
        self.kv_rate = KeyValueFrame(master=self.left_frame, key="Taux Agios:", value=self.binding.poucentage_agios)


class InputBarFrame(tk.Frame):
    def __init__(self, master=None, on_click_retrait=None, on_click_versement=None):
        super().__init__(master, height=20)
        self.master = master
        # self.config(background="red")
        self.pack(side=tk.BOTTOM, fill=tk.X, expand=False)
        self.create_widgets()

    def validate_float(self, new_text):
        if not new_text:  # the field is being cleared
            return True
        try:
            float(new_text)
            return True
        except ValueError:
            return False

    def create_widgets(self):
        self.input = tk.Entry(self, validate="key")
        self.input['validatecommand'] = (self.input.register(self.validate_float), '%P')
        self.input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=Padding.MEDIUM.value, pady=Padding.MEDIUM.value)

        self.button_frame = tk.Frame(self)
        self.button_frame.pack(side=tk.RIGHT, fill=tk.X, expand=False)

        self.versement_button = tk.Button(self.button_frame,
                                          command=self.master.on_click_versement,
                                          text="Versement",
                                          width=15)
        self.versement_button.pack(side=tk.LEFT, padx=Padding.MEDIUM.value, pady=Padding.MEDIUM.value)

        self.retrait_button = tk.Button(self.button_frame,
                                        command=self.master.on_click_retrait,
                                        text="Retrait",
                                        width=15)
        self.retrait_button.pack(side=tk.LEFT, padx=Padding.MEDIUM.value, pady=Padding.MEDIUM.value)


class AccountLogFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        # self.config(background="blue")
        self.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.create_widgets()

    def insert_log(self, date, operation, nouveau_solde):
        self.tree.insert('', 'end', text="Item 1", values=(date, operation, nouveau_solde))

    def create_widgets(self):
        self.tree = ttk.Treeview(self, columns=('date', 'operation', 'nouveau_solde'), show='headings')
        self.tree.heading('date', text='Date')
        self.tree.heading('operation', text='Opération')
        self.tree.heading('nouveau_solde', text='Nouveau solde')

        self.scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side='right', fill='y')

        # Add items to the tree
        self.tree.insert('', 'end', text="Item 1", values=("10/10/2021", "Deposit", "100.00"))
        self.tree.insert('', 'end', text="Item 2", values=("11/10/2021", "Withdrawal", "50.00"))
        self.tree.insert('', 'end', text="Item 1", values=("10/10/2021", "Deposit", "100.00"))


class Application(tk.Frame):
    def __init__(self, master=None, state=None):
        super().__init__(master)
        self.master = master
        self.state = state
        self.bindings = CompteCourantBinding(self.state.compteCourant, master=master)
        master.geometry(DEFAULT_WINDOW_GEOMETRY)
        # master.config(background="green")
        # self.config(background="purple")
        self.pack(side=tk.TOP,
                  fill=tk.BOTH,
                  expand=True,
                  padx=Padding.MEDIUM.value,
                  pady=Padding.TINY.value)
        self.create_title_frame()
        self.create_account_info_frame()
        self.create_account_log_frame()
        self.create_input_bar_frame()
        # self.create_widgets()

    def on_click_retrait(self):
        montant = 100
        self.state.compteCourant.retrait(montant)
        dt = datetime.now()
        self.account_log_frame.insert_log(dt.strftime("%d/%m/%Y"), f"Retrait / {montant} EUR",
                                          self.state.compteCourant.solde)
        self.bindings.update()

    def on_click_versement(self):
        self.account_log_frame.insert_log("10/10/2021", "Versement", "100.00")

    def create_input_bar_frame(self):
        self.input_bar_frame = InputBarFrame(master=self, on_click_retrait=self.on_click_retrait,
                                             on_click_versement=self.on_click_versement)

    def create_title_frame(self):
        self.titleFrame = tk.Frame(self)
        # self.titleFrame.config(background="yellow")
        self.titleFrame.pack(side=tk.TOP, fill=tk.X)

        self.title = tk.Label(self.titleFrame, text="Compte Courant", font=TITLE_FONT, anchor="w")
        self.title.pack(side=tk.LEFT, padx=Padding.MEDIUM.value, pady=Padding.MEDIUM.value)

    def create_account_info_frame(self):
        self.account_info_frame = AccountInfoFrame(self.bindings, master=self)

    def create_account_log_frame(self):
        self.account_log_frame = AccountLogFrame(master=self)

    def create_widgets(self):
        self.hello = tk.Button(self)
        self.hello["text"] = "Hello World\n(click me)"
        self.hello["command"] = self.say_hello
        self.hello.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hello(self):
        print("Hello World!")


def main():
    state = State()
    root = tk.Tk()
    root.title("Gestion de comptes")
    app = Application(master=root, state=state)
    app.mainloop()


if __name__ == "__main__":
    main()