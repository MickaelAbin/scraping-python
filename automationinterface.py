import pyautogui

# Obtient la résolution de l'écran
ecran_largeur, ecran_hauteur = pyautogui.size()

# Affiche la résolution
print(f"Résolution de l'écran: {ecran_largeur}x{ecran_hauteur}")




# # Déplace la souris en (x=100, y=200) sur l'écran
# pyautogui.moveTo(960, 540)


# Vous pouvez également spécifier les coordonnées pour le clic droit
x, y = 1000, 300
pyautogui.click(x, y, button='left')
# Écrit "Bonjour !" avec un intervalle d'1 seconde entre chaque caractère
pyautogui.write('Bonjour !', interval=1)

pyautogui.hotkey('ctrl', 'a')
pyautogui.sleep(2)
pyautogui.press('delete')

pyautogui.write('Dans le cul', interval=0.5)