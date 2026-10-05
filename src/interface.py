import tkinter as tk

root = tk.Tk()

root.geometry("500x500")
root.iconbitmap("../assets/icon.ico")

button_start = tk.Button(root, text="Start")
button_start.pack()

root.mainloop()