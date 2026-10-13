"""import tkinter as tk

score = 0

def start():
    global score
    score += 1
    label.config(text=str(score))

root = tk.Tk()

root.geometry("500x500")
root.iconbitmap("../assets/icon.ico")

header = tk.Frame(root, bg="black", height=100, width=400)
header.pack(side="top", fill="x")

footer = tk.Frame(root, bg="black", height=100, width=400)
footer.pack(side="bottom", fill="x")

main = tk. Frame(root, bg="light blue", height=400, width=400)
main.pack(side="bottom", fill="x")

button_start = tk.Button(main, text="Start", command=start)
button_start.pack()

label = tk.Label(header, text=0, height=2, width=10)
label.pack()

entry = tk.Entry(header)
entry.pack()

root.mainloop()"""

"""import tkinter as tk

root = tk.Tk()

root.geometry('500x500')
root.title('КАЛЬКУЛЯТОР ТОП')
root.configure(background='black')

result = ''
first_stage = 0

def insert_value(value):
    global result
    result = result + f'{value}'
    print(result)
    input_text.config(text=result)


def operations(value):
    global result, first_stage
    if first_stage == 0:
        first_stage = int(result)
        result = str(f"{first_stage} {value} ")
        input_text.config(text=result)
    elif value == '=':
        one_digit = ''
        two_digit = ''
        operator = ''
        step = 0
        for o in result:
            if o == '+' or o == '-':
                operator = o

        for i in result:
            if i != operator:
                one_digit += i
                step += 1
            else:
                break

        for j, k in enumerate(result):
            if j > step:
                if k != operator:
                    two_digit += k
        result = int(one_digit) + int(two_digit)
        input_text.config(text=result)


def init():
    frame_top = tk.Frame(root, width=500, height=100, background='grey')
    frame_bottom_left = tk.Frame(root, width=350, height=100)
    frame_bottom_right = tk.Frame(root, width=150, height=100, background='grey')
    return [frame_top, frame_bottom_left, frame_bottom_right]


def gui():
    global input_text

    frames = init()
    frames[0].pack(side="top", padx=25, pady=15)
    frames[1].pack(side="left", padx=25, pady=15)
    frames[2].pack(side="right", padx=25, pady=15)
    col = 0
    row = 0

    input_text = tk.Label(frames[0], width=40, height=3)
    input_text.pack()

    for step in range(10):
        button = tk.Button(frames[1], text=step, width=10, height=5, command=lambda value=step: insert_value(value))
        button.grid(column=col, row=row)
        col += 1
        if col == 3:
            col = 0
            row += 1
    dot = tk.Button(frames[1], text='.', width=10, height=5, command=lambda value='.': insert_value(value))
    dot.grid(column=col, row=row)
    col = 0
    row = 0

    list_operators = ["*", "%", "-", "+", "=", "c"]
    for operator in list_operators:
        operator = tk.Button(frames[2], text=operator, width=15, height=3, command= lambda val=operator: operations(val))
        operator.pack()


gui()
root.mainloop()"""

import tkinter as tk

root = tk.Tk()
root.geometry('400x400')
root.iconbitmap('../assets/icon.ico')

collection = ["task_1 | create menu", "task_2 | add main", "task_3 | update main", "task_4 | delete main"]

frame_menu = None
frame_tasks = None

tasks = None

def main():
    global frame_menu, frame_tasks, tasks
    frame_menu = tk.Frame(root, background="black", width=400, height=400)
    frame_tasks = tk.Frame(root, background="black", width=400, height=400)
    frame_menu.pack_propagate(False)
    frame_tasks.pack_propagate(False)

    button_show_tasks = tk.Button(frame_menu, text="Посмотреть все задачи", command=show_all_tasks)
    button_show_tasks.pack()

    button_exit = tk.Button(frame_tasks, text="Exit", command=create_menu)
    button_exit.pack()

    tasks = tk.Listbox(frame_tasks)
    tasks.pack()

def show_all_tasks():
    frame_menu.pack_forget()
    frame_tasks.pack()

    tasks.delete(0, tk.END)

    for number, content in enumerate(collection):
        word = ''
        for symbol in content:
            if symbol != '|':
                word = f"{word}{symbol}"
            else:
                break
        tasks.insert(tk.END, word)

def create_menu():
    frame_tasks.pack_forget()
    frame_menu.pack()

main()
create_menu()
root.mainloop()
