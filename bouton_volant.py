import tkinter as tk
import random
import pyautogui
import pygame

def play_sound(file_path, volume=1.0):
    sound = pygame.mixer.Sound(file_path)
    sound.set_volume(volume)
    channel = pygame.mixer.find_channel()  # Trouve un canal disponible
    channel.set_volume(volume)
    channel.play(sound)
sound = "C:\\Users\\EPSI\\Documents\\cri_babouchka.mp3"

pygame.mixer.init()


def Creer_bouton():
        def move_button():
            new_x = random.randint(0, window.winfo_width() - button.winfo_width())
            new_y = random.randint(0, window.winfo_height() - button.winfo_height())
            button.place(x=new_x, y=new_y)
            play_sound(sound)
        def on_enter(event):
            button.config(relief=tk.RIDGE)
            move_button()
        def on_leave(event):
            button.config(relief=tk.FLAT)
        button = tk.Button(window, text="Couper le son", command= Creer_bouton, relief=tk.FLAT)
        button.pack(pady=20)
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
screen_width, screen_height = pyautogui.size()
center_x, center_y = screen_width // 4, screen_height // 4


# Création de la fenêtre
window = tk.Tk()
window.title("Essaye encore")
window.geometry(f"800x450+{center_x}+{center_y}")

# Création d'un Frame dans la fenêtre principale
frame = tk.Frame(window)
frame.pack()

# Création du bouton
button2 = tk.Button(frame, text="Ne pas cliquez ici", command = Creer_bouton)
button2.pack()



# Boucle principale
window.mainloop()
