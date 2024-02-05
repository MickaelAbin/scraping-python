# import os

# Chemin local (local path)
# current_directory = os.getcwd()
# print("Chemin local (local path):", current_directory)

# # Liste des fichiers dans le répertoire courant
# file_list = os.listdir(current_directory)
# print("Liste des fichiers dans le répertoire courant:", file_list)

# chemin_parent = os.path.join(os.getcwd(), '..')
# print("Chemin vers le répertoire parent :", chemin_parent)

# import os
# import pwd

# # Chemin du fichier ou du répertoire
# chemin = '/chemin/vers/votre/fichier'

# # Obtenir les informations sur le propriétaire
# stat_info = os.stat(chemin)
# uid = stat_info.st_uid

# # Obtenir le nom de l'utilisateur
# proprietaire = pwd.getpwuid(uid)
# print("Nom du propriétaire:", proprietaire.pw_name)

# import threading

# class MyThread(threading.Thread):
#     def run(self):
#         print("Thread en cours d'exécution")

# if __name__ == "__main__":
#     thread = MyThread()
#     thread.start()

# import threading

# shared_variable = 0
# lock = threading.Lock()

# def increment_shared_variable():
#     global shared_variable
#     with lock:
#         shared_variable += 1

# if __name__ == "__main__":
#     threads = []
#     for _ in range(5):
#         thread = threading.Thread(target=increment_shared_variable)
#         threads.append(thread)
#         print(thread)
#         thread.start()

#     for thread in threads:
#         thread.join()

#     print("Valeur partagée:", shared_variable)


import asyncio

async def task1():
    await asyncio.sleep(2)
    print("Tâche 1 terminée")

async def task2():
    await asyncio.sleep(1)
    print("Tâche 2 terminée")

async def main():
    await asyncio.gather(task1(), task2())

if __name__ == "__main__":
    asyncio.run(main())



