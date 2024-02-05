import tkinter as tk

root = tk.Tk()

frame = tk.Frame(root)
frame.pack()

btn1 = tk.Button(frame, text="Haut", bg="red")
btn1.pack(side=tk.TOP)

btn2 = tk.Button(frame, text="Bas", bg="green")
btn2.pack(side=tk.BOTTOM)

btn3 = tk.Button(frame, text="Gauche", bg="blue")
btn3.pack(side=tk.LEFT)

btn4 = tk.Button(frame, text="Droite", bg="yellow")
btn4.pack(side=tk.RIGHT)

frame2 = tk.Frame(root)
frame2.pack()

btn1 = tk.Button(frame2, text="Haut", bg="red")
btn1.pack(side=tk.TOP)

btn2 = tk.Button(frame2, text="Bas", bg="green")
btn2.pack(side=tk.BOTTOM)

btn3 = tk.Button(frame2, text="Gauche", bg="blue")
btn3.pack(side=tk.LEFT)

btn4 = tk.Button(frame2, text="Droite", bg="yellow")
btn4.pack(side=tk.RIGHT)
root.mainloop()
