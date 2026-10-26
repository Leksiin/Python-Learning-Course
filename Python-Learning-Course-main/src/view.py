"""
    ======================================================
        Модуль который отображает графический интерфейс
    ======================================================
"""

from ui.Interface import Interface
collection = load_file([], NAME_FILE_SAVES)
ui = Interface()

def main():
    ui.list_task.bind("<<ListboxSelect>>", show_details)
    show_all_tasks()

def show_all_tasks():

    for number, content in enumerate(collection):
        print(number, content)
        ui.list_task.add_to_list(content["name"])


def show_details(event=None):
    cur_task = ui.list_task.curselection()
    task = collection[cur_task[0]]
    ui.create_top(task["name"], task["content"], task["author"])



main()
ui.root.mainloop()
