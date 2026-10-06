import tkinter as tk

numbers = []

def config():
    numbers.append()

def multiply():
    pass

def divide():
    pass

def summ():
    pass

def diff():
    pass

def result():
    pass

# Главный холст
root = tk.Tk()

root.geometry("400x200")
root.iconbitmap("../assets/icon.ico")

# Верхняя панель
top_frame = tk.Frame(root, height=150, bg="midnightblue", padx=10, pady=10)
top_frame.pack(fill='x', side='top')

# Нижняя панель
bottom_frame = tk.Frame(root, height=300, bg="midnightblue", padx=10, pady=30)
bottom_frame.pack(fill='x', side='bottom')

list_buttons = []

for i in range(10):
    b = (tk.Button(bottom_frame))
    b.pack(side='left')
    b.config(text=str(i))

states = [ ['multiply', '*'],
           ['summ', '+'],
           ['diff', '-'],
           ['divide', '%'],
           ['result', '='] ]

for state in states:
    b = (tk.Button(bottom_frame))
    b.pack(side='right')
    b.config(command=state[0], text=state[1])

input_text = tk.Label(top_frame, text=" ")
input_text.pack(side='left')

result_text = tk.Label(top_frame, text=" ")
result_text.pack(side='right')

# Запуск
root.mainloop()
